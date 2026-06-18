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

            const docLinks = document.querySelectorAll('.doc-link[href]');

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
        document.querySelectorAll('.doc-link[href]').forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const href = link.getAttribute('href');

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
                loadAndShowMarkdown('../README.md', 'About Project');
            });
        }

        // Theme Switcher Logic
        const themeNav = document.getElementById('nav-theme');
        const themeIconSun = document.getElementById('theme-icon-sun');
        const themeIconMoon = document.getElementById('theme-icon-moon');
        const themeText = document.getElementById('theme-text');
        const htmlElement = document.documentElement;
        const THEME_STORAGE_KEY = 'sonata-theme';

        function applyTheme(theme) {
            htmlElement.classList.remove('light', 'dark');
            htmlElement.classList.add(theme);
            if (theme === 'dark') {
                if (themeIconSun) themeIconSun.classList.add('hidden');
                if (themeIconMoon) themeIconMoon.classList.remove('hidden');
                if (themeText) themeText.textContent = 'Light mode';
            } else {
                if (themeIconSun) themeIconSun.classList.remove('hidden');
                if (themeIconMoon) themeIconMoon.classList.add('hidden');
                if (themeText) themeText.textContent = 'Dark mode';
            }
            localStorage.setItem(THEME_STORAGE_KEY, theme);
        }

        // Load saved theme on page load
        const savedTheme = localStorage.getItem(THEME_STORAGE_KEY);
        if (savedTheme === 'dark') {
            applyTheme('dark');
        }

        if (themeNav) {
            themeNav.addEventListener('click', (e) => {
                e.preventDefault();
                // Enable smooth transitions temporarily
                htmlElement.classList.add('smooth-theme-transition');
                const isDark = htmlElement.classList.contains('dark');
                applyTheme(isDark ? 'light' : 'dark');
                // Remove transition class after animation completes
                setTimeout(() => {
                    htmlElement.classList.remove('smooth-theme-transition');
                }, 400);
            });
        }

        // Section Navigation (smooth scroll)
        document.querySelectorAll('.nav-section').forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const targetId = link.getAttribute('data-section');
                const target = document.getElementById(targetId);
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                    // Close sidebar on mobile
                    if (sidebar) {
                        sidebar.classList.add('-translate-x-full');
                        overlay.classList.add('hidden');
                    }
                }
            });
        });

        // Get Started nav handler
        const getStartedNav = document.getElementById('nav-get-started');
        if (getStartedNav) {
            getStartedNav.addEventListener('click', (e) => {
                e.preventDefault();
                window.scrollTo({ top: 0, behavior: 'smooth' });
                if (sidebar) {
                    sidebar.classList.add('-translate-x-full');
                    overlay.classList.add('hidden');
                }
            });
        }

        // Quick "About the Project" button in Get Started section
        const btnAboutQuick = document.getElementById('btn-about-quick');
        if (btnAboutQuick) {
            btnAboutQuick.addEventListener('click', (e) => {
                e.preventDefault();
                loadAndShowMarkdown('../README.md', 'About Project');
            });
        }

// Gallery Data
const galleryItems = [
    { src: 'assets/diagrams/project_boundary.svg', title: 'Project Boundary', category: 'Architecture' },
    { src: 'assets/diagrams/public_private_boundary.svg', title: 'Disclosure Boundary', category: 'Front Matter' },
    { src: 'assets/diagrams/layered_architecture.svg', title: 'Layered Architecture', category: 'Architecture' },
    { src: 'assets/diagrams/backend_ladder.svg', title: 'Backend Dispatch Chain', category: 'GPU Execution' },
    { src: 'assets/diagrams/autograd_mamba_flow.svg', title: 'Autograd + Mamba Flow', category: 'Integration' },
    { src: 'assets/diagrams/logos_control_loop.svg', title: 'Symbolic Control Loop', category: 'Logos' },
    { src: 'assets/diagrams/benchmark_timeline.svg', title: 'Benchmark Timeline', category: 'Benchmark Correction' },
    { src: 'assets/diagrams/hardware_constraint_panel.svg', title: 'Hardware Constraints', category: 'Limitations' },
    { src: 'assets/plots/throughput_comparison.svg', title: 'Throughput Comparison', category: 'Training Results' },
    { src: 'assets/plots/vram_usage.svg', title: 'VRAM Usage', category: 'Training Results' },
    { src: 'assets/plots/h2d_traffic_reduction.svg', title: 'H2D Traffic', category: 'GPU Execution' },
    { src: 'assets/plots/int8_validation.svg', title: 'INT8 Validation', category: 'Quantization' },
    { src: 'assets/plots/stability_throughput.svg', title: 'Stability & Throughput', category: 'Benchmark Correction' },
];

// Gallery State
let galleryIndex = 0;
let galleryMode = 'carousel';

// Gallery DOM
const galleryModal = document.getElementById('gallery-modal');
const galleryMainImg = document.getElementById('gallery-main-img');
const gallerySideLeft = document.getElementById('gallery-side-left');
const gallerySideRight = document.getElementById('gallery-side-right');
const galleryCaption = document.getElementById('gallery-caption');
const galleryCarousel = document.getElementById('gallery-carousel');
const galleryGrid = document.getElementById('gallery-grid');
const galleryModeBtn = document.getElementById('gallery-mode-btn');
const galleryModeText = document.getElementById('gallery-mode-text');
const galleryModeDropdown = document.getElementById('gallery-mode-dropdown');
const galleryPrev = document.getElementById('gallery-prev');
const galleryNext = document.getElementById('gallery-next');
const galleryClose = document.getElementById('gallery-close');
const openGalleryBtn = document.getElementById('open-gallery');

function renderGallery() {
    const item = galleryItems[galleryIndex];
    galleryMainImg.src = item.src;
    galleryMainImg.alt = item.title;
    galleryCaption.textContent = `${galleryIndex + 1} / ${galleryItems.length} — ${item.title}`;
    const leftIdx = galleryIndex > 0 ? galleryIndex - 1 : galleryItems.length - 1;
    const rightIdx = galleryIndex < galleryItems.length - 1 ? galleryIndex + 1 : 0;
    gallerySideLeft.querySelector('img').src = galleryItems[leftIdx].src;
    gallerySideLeft.querySelector('img').alt = galleryItems[leftIdx].title;
    gallerySideRight.querySelector('img').src = galleryItems[rightIdx].src;
    gallerySideRight.querySelector('img').alt = galleryItems[rightIdx].title;
    galleryPrev.style.display = galleryItems.length <= 1 ? 'none' : '';
    galleryNext.style.display = galleryItems.length <= 1 ? 'none' : '';
    document.querySelectorAll('.gallery-grid-thumb').forEach((thumb, i) => {
        thumb.classList.toggle('active', i === galleryIndex);
    });
}

function buildGrid() {
    const container = galleryGrid.querySelector('.grid');
    container.innerHTML = '';
    galleryItems.forEach((item, i) => {
        const div = document.createElement('div');
        div.className = 'gallery-grid-thumb';
        div.innerHTML = `<img src="${item.src}" alt="${item.title}"/>`;
        div.addEventListener('click', () => {
            galleryIndex = i;
            setMode('carousel');
        });
        container.appendChild(div);
    });
}

function setMode(mode) {
    galleryMode = mode;
    if (mode === 'carousel') {
        galleryCarousel.classList.remove('hidden');
        galleryGrid.classList.add('hidden');
        galleryModeText.textContent = 'Grid';
        document.getElementById('gallery-mode-icon').innerHTML = '<rect x="1" y="1" width="6" height="6" rx="1"/><rect x="9" y="1" width="6" height="6" rx="1"/><rect x="1" y="9" width="6" height="6" rx="1"/><rect x="9" y="9" width="6" height="6" rx="1"/>';
    } else {
        galleryCarousel.classList.add('hidden');
        galleryGrid.classList.remove('hidden');
        galleryModeText.textContent = 'Carousel';
        document.getElementById('gallery-mode-icon').innerHTML = '<rect x="1" y="3" width="14" height="10" rx="2"/><circle cx="8" cy="8" r="2"/>';
    }
    galleryModeDropdown.classList.add('hidden');
    renderGallery();
}

function openGallery(startIndex) {
    galleryIndex = startIndex || 0;
    setMode('carousel');
    galleryModal.classList.remove('hidden');
    void galleryModal.offsetWidth;
    galleryModal.classList.remove('opacity-0');
    document.body.style.overflow = 'hidden';
    renderGallery();
}

function closeGallery() {
    galleryModal.classList.add('opacity-0');
    setTimeout(() => {
        galleryModal.classList.add('hidden');
        document.body.style.overflow = '';
    }, 300);
}

if (openGalleryBtn) {
    openGalleryBtn.addEventListener('click', () => openGallery(0));
}

if (galleryClose) {
    galleryClose.addEventListener('click', closeGallery);
}

if (galleryModal) {
    galleryModal.addEventListener('click', (e) => {
        if (e.target === galleryModal) closeGallery();
    });
}

if (galleryPrev) {
    galleryPrev.addEventListener('click', () => {
        galleryIndex = galleryIndex > 0 ? galleryIndex - 1 : galleryItems.length - 1;
        renderGallery();
    });
}

if (galleryNext) {
    galleryNext.addEventListener('click', () => {
        galleryIndex = galleryIndex < galleryItems.length - 1 ? galleryIndex + 1 : 0;
        renderGallery();
    });
}

if (gallerySideLeft) {
    gallerySideLeft.addEventListener('click', () => {
        galleryIndex = galleryIndex > 0 ? galleryIndex - 1 : galleryItems.length - 1;
        renderGallery();
    });
}

if (gallerySideRight) {
    gallerySideRight.addEventListener('click', () => {
        galleryIndex = galleryIndex < galleryItems.length - 1 ? galleryIndex + 1 : 0;
        renderGallery();
    });
}

if (galleryModeBtn) {
    galleryModeBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        galleryModeDropdown.classList.toggle('hidden');
    });
}

document.querySelectorAll('.gallery-mode-option').forEach(option => {
    option.addEventListener('click', () => {
        setMode(option.getAttribute('data-mode'));
    });
});

document.addEventListener('click', (e) => {
    if (!galleryModeBtn.contains(e.target) && !galleryModeDropdown.contains(e.target)) {
        galleryModeDropdown.classList.add('hidden');
    }
});

document.addEventListener('keydown', (e) => {
    if (galleryModal.classList.contains('hidden')) return;
    if (e.key === 'Escape') closeGallery();
    if (galleryMode === 'carousel') {
        if (e.key === 'ArrowLeft') {
            galleryIndex = galleryIndex > 0 ? galleryIndex - 1 : galleryItems.length - 1;
            renderGallery();
        }
        if (e.key === 'ArrowRight') {
            galleryIndex = galleryIndex < galleryItems.length - 1 ? galleryIndex + 1 : 0;
            renderGallery();
        }
    }
});

buildGrid();
