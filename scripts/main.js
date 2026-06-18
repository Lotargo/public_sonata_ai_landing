        // Simple mobile menu toggle
        const openBtn = document.getElementById('open-sidebar');
        const closeBtn = document.getElementById('close-sidebar');
        const sidebar = document.getElementById('sidebar');
        const overlay = document.getElementById('mobile-menu-overlay');

        function toggleMenu() {
            sidebar.classList.toggle('-translate-x-full');
            overlay.classList.toggle('hidden');
        }

        if(openBtn && closeBtn && sidebar && overlay) {
            openBtn.addEventListener('click', toggleMenu);
            closeBtn.addEventListener('click', toggleMenu);
            overlay.addEventListener('click', toggleMenu);
        }

        // Document Modal Logic
        const docModal = document.getElementById('doc-modal');
        const docModalContent = document.getElementById('doc-modal-content');
        const docModalBody = document.getElementById('doc-modal-body');
        const docModalTitle = document.getElementById('doc-modal-title');
        const closeDocModalBtn = document.getElementById('close-doc-modal');

        function openDocModal() {
            docModal.classList.remove('hidden');
            docModal.classList.add('flex');
            // Trigger reflow
            void docModal.offsetWidth;
            docModal.classList.remove('opacity-0');
            docModalContent.classList.remove('scale-95');
            document.body.style.overflow = 'hidden'; // Prevent background scrolling
        }

        function closeDocModal() {
            docModal.classList.add('opacity-0');
            docModalContent.classList.add('scale-95');
            setTimeout(() => {
                docModal.classList.remove('flex');
                docModal.classList.add('hidden');
                document.body.style.overflow = '';
            }, 300); // match duration-300
        }

        if (closeDocModalBtn) {
            closeDocModalBtn.addEventListener('click', closeDocModal);
        }

        // Close modal when clicking outside the content
        if (docModal) {
            docModal.addEventListener('click', (e) => {
                if (e.target === docModal) {
                    closeDocModal();
                }
            });
        }

        // Print/Export Modal Logic
        const printNav = document.getElementById('nav-print');
        const printModal = document.getElementById('print-modal');
        const printModalContent = document.getElementById('print-modal-content');
        const closePrintModalBtn = document.getElementById('close-print-modal');
        const cancelPrintBtn = document.getElementById('cancel-print-btn');
        const printCheckboxesContainer = document.getElementById('print-checkboxes');
        const printForm = document.getElementById('print-form');
        const printArea = document.getElementById('print-area');

        function openPrintModal() {
            // Populate checkboxes based on current document links on the page
            printCheckboxesContainer.innerHTML = '';

            const docLinks = document.querySelectorAll('a[href^="docs/"]');

            if (docLinks.length === 0) {
                 printCheckboxesContainer.innerHTML = '<p class="text-sm text-secondary">No documents found to print.</p>';
            } else {
                docLinks.forEach((link, index) => {
                    const title = link.textContent.trim();
                    let mdFile = link.getAttribute('href');
                    if (mdFile.endsWith('.html')) {
                        mdFile = mdFile.substring(0, mdFile.length - 5) + '.md';
                    }

                    const checkboxId = `print-doc-${index}`;

                    const div = document.createElement('div');
                    div.className = 'flex items-center gap-2';
                    div.innerHTML = `
                        <input type="checkbox" id="${checkboxId}" value="${mdFile}" data-title="${title}" class="rounded border-outline-variant text-primary focus:ring-primary w-4 h-4 cursor-pointer" checked>
                        <label for="${checkboxId}" class="text-sm cursor-pointer select-none">${title}</label>
                    `;
                    printCheckboxesContainer.appendChild(div);
                });
            }

            printModal.classList.remove('hidden');
            printModal.classList.add('flex');
            void printModal.offsetWidth; // Trigger reflow
            printModal.classList.remove('opacity-0');
            printModalContent.classList.remove('scale-95');
            document.body.style.overflow = 'hidden';
        }

        function closePrintModal() {
            printModal.classList.add('opacity-0');
            printModalContent.classList.add('scale-95');
            setTimeout(() => {
                printModal.classList.remove('flex');
                printModal.classList.add('hidden');
                document.body.style.overflow = '';
            }, 300);
        }

        if (printNav) {
            printNav.addEventListener('click', (e) => {
                e.preventDefault();
                openPrintModal();
            });
        }

        if (closePrintModalBtn) closePrintModalBtn.addEventListener('click', closePrintModal);
        if (cancelPrintBtn) cancelPrintBtn.addEventListener('click', closePrintModal);

        if (printModal) {
            printModal.addEventListener('click', (e) => {
                if (e.target === printModal) {
                    closePrintModal();
                }
            });
        }

        if (printForm) {
            printForm.addEventListener('submit', async (e) => {
                e.preventDefault();

                const selectedCheckboxes = printCheckboxesContainer.querySelectorAll('input[type="checkbox"]:checked');
                if (selectedCheckboxes.length === 0) {
                    alert("Please select at least one document to print.");
                    return;
                }

                // Temporary loading state on the button
                const submitBtn = document.getElementById('submit-print-btn');
                const originalBtnContent = submitBtn.innerHTML;
                submitBtn.innerHTML = '<div class="animate-spin rounded-full h-5 w-5 border-b-2 border-on-primary"></div> Generating...';
                submitBtn.disabled = true;

                printArea.innerHTML = ''; // Clear previous print content

                try {
                    for (const checkbox of selectedCheckboxes) {
                        const mdFile = checkbox.value;
                        const title = checkbox.getAttribute('data-title');

                        const response = await fetch(mdFile);
                        if (!response.ok) throw new Error(`HTTP error fetching ${mdFile}: ${response.status}`);
                        const markdownText = await response.text();

                        let processedMarkdown = markdownText.replace(/```mermaid\n([\s\S]*?)```/g, '<div class="mermaid">\n$1\n</div>');
                        const htmlContent = marked.parse(processedMarkdown);

                        const docContainer = document.createElement('div');
                        docContainer.className = 'print-document markdown-body mb-8 page-break-after';
                        // Add title if it's not already the main h1 of the document
                        docContainer.innerHTML = htmlContent;
                        printArea.appendChild(docContainer);
                    }

                    // Wait for rendering libraries
                    if (window.MathJax) {
                        await MathJax.typesetPromise([printArea]).catch((err) => console.error('MathJax print error:', err));
                    }

                    if (window.mermaid) {
                        mermaid.run({
                            nodes: printArea.querySelectorAll('.mermaid')
                        });
                        // Mermaid rendering is async but doesn't return a promise nicely in all versions.
                        // Adding a slight delay to ensure SVGs are generated before print dialog opens.
                        await new Promise(resolve => setTimeout(resolve, 500));
                    }

                    closePrintModal();

                    // Small delay to ensure modal is gone before printing
                    setTimeout(() => {
                        window.print();
                    }, 400);

                } catch (error) {
                    console.error("Print generation failed:", error);
                    alert("Failed to generate print documents. See console for details.");
                } finally {
                    submitBtn.innerHTML = originalBtnContent;
                    submitBtn.disabled = false;
                }
            });
        }

        async function loadAndShowMarkdown(mdFile, title) {
            // Show loading state
            docModalTitle.textContent = title || 'Loading Document...';
            docModalBody.innerHTML = `
                <div class="flex justify-center items-center h-full">
                    <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-primary"></div>
                </div>
            `;
            openDocModal();

            try {
                const response = await fetch(mdFile);
                if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
                const markdownText = await response.text();

                // Pre-process markdown for Mermaid blocks to make them div.mermaid instead of pre/code
                let processedMarkdown = markdownText.replace(/```mermaid\n([\s\S]*?)```/g, '<div class="mermaid">\n$1\n</div>');

                // Parse markdown to HTML
                const htmlContent = marked.parse(processedMarkdown);

                // Inject into modal
                docModalBody.innerHTML = htmlContent;

                // Render LaTeX (MathJax)
                if (window.MathJax) {
                    MathJax.typesetPromise([docModalBody]).catch((err) => console.error('MathJax error:', err));
                }

                // Render Mermaid diagrams
                if (window.mermaid) {
                    mermaid.run({
                        nodes: docModalBody.querySelectorAll('.mermaid')
                    });
                }

            } catch (error) {
                console.error("Failed to load document:", error);
                docModalBody.innerHTML = `<div class="text-error p-4 bg-error-container rounded border border-error">Failed to load document. ${error.message}</div>`;
            }
        }

        // Intercept document links
        document.querySelectorAll('a[href^="docs/"]').forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const href = link.getAttribute('href');

                // Assuming links are like docs/filename.html but actual files are docs/filename.md
                let mdFile = href;
                if (mdFile.endsWith('.html')) {
                    mdFile = mdFile.substring(0, mdFile.length - 5) + '.md';
                }

                loadAndShowMarkdown(mdFile, link.textContent.trim());
            });
        });

        // About modal
        const aboutNav = document.getElementById('nav-about');
        if (aboutNav) {
            aboutNav.addEventListener('click', (e) => {
                e.preventDefault();
                loadAndShowMarkdown('README.md', 'About Project');
            });
        }

        // Theme Switcher Logic
        const themeNav = document.getElementById('nav-theme');
        const themeIcon = document.getElementById('theme-icon');
        const themeText = document.getElementById('theme-text');
        const htmlElement = document.documentElement;

        if (themeNav) {
            themeNav.addEventListener('click', (e) => {
                e.preventDefault();
                const isDark = htmlElement.classList.contains('dark');

                if (isDark) {
                    htmlElement.classList.remove('dark');
                    htmlElement.classList.add('light');
                    if (themeIcon) themeIcon.textContent = 'dark_mode';
                    if (themeText) themeText.textContent = 'Dark mode';
                } else {
                    htmlElement.classList.remove('light');
                    htmlElement.classList.add('dark');
                    if (themeIcon) themeIcon.textContent = 'light_mode';
                    if (themeText) themeText.textContent = 'Light mode';
                }
            });
        }
