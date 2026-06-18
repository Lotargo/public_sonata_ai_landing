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

        // Intercept document links
        document.querySelectorAll('a[href^="docs/"]').forEach(link => {
            link.addEventListener('click', async (e) => {
                e.preventDefault();
                const href = link.getAttribute('href');

                // Assuming links are like docs/filename.html but actual files are docs/filename.md
                let mdFile = href;
                if (mdFile.endsWith('.html')) {
                    mdFile = mdFile.substring(0, mdFile.length - 5) + '.md';
                }

                // Show loading state
                docModalTitle.textContent = link.textContent.trim() || 'Loading Document...';
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
            });
        });
