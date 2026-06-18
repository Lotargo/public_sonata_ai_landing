import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

OUTPUT = os.path.dirname(os.path.abspath(__file__))

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 12,
    'axes.labelsize': 13,
    'axes.titlesize': 14,
    'axes.titleweight': 'bold',
    'font.weight': 'normal',
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.2,
    'axes.grid': True,
    'grid.alpha': 0.25,
    'grid.linewidth': 0.6,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

COLORS = {
    'blue': '#3B82F6',
    'green': '#22C55E',
    'red': '#EF4444',
    'orange': '#F59E0B',
    'purple': '#A855F7',
    'grey': '#9CA3AF',
    'light_grey': '#F3F4F6',
    'dark': '#1F2937',
    'white': '#FFFFFF',
    'blue_fill': '#DBEAFE',
    'green_fill': '#DCFCE7',
    'red_fill': '#FEE2E2',
    'orange_fill': '#FEF3C7',
    'purple_fill': '#F3E8FF',
    'grey_fill': '#F9FAFB',
}

def save(path, fig=None):
    if fig is None:
        fig = plt.gcf()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fig.savefig(path, facecolor='white', edgecolor='none')
    plt.close(fig)
    print(f"  Saved: {os.path.relpath(path, OUTPUT)}")

def thumbnail(src_path):
    thumb_dir = os.path.join(OUTPUT, 'thumbnails')
    os.makedirs(thumb_dir, exist_ok=True)
    name = os.path.basename(src_path)
    thumb_path = os.path.join(thumb_dir, name)
    from PIL import Image
    img = Image.open(src_path)
    img.thumbnail((480, 360), Image.LANCZOS)
    img.save(thumb_path)
    print(f"  Thumbnail: {os.path.relpath(thumb_path, OUTPUT)}")

# ─── DIAGRAMS ────────────────────────────────────────────────

def diagram_project_boundary():
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_xlim(0, 12); ax.set_ylim(0, 8.5)
    ax.axis('off')

    left = mpatches.FancyBboxPatch((0.4, 0.5), 5.0, 7.2, boxstyle="round,pad=0.2",
                                     facecolor=COLORS['blue_fill'], edgecolor=COLORS['blue'], linewidth=2.5)
    ax.add_patch(left)
    ax.text(2.9, 7.4, 'Sonata IS', ha='center', va='bottom', fontsize=16, fontweight='bold', color=COLORS['blue'])
    items_is = [
        'Laboratory research platform',
        'Custom tensor/autograd/runtime stack',
        'Heterogeneous CPU/GPU execution',
        'Training & inference experiments',
        'INT8 quantization path',
        'Mamba-style sequence modeling',
        'Early symbolic-control bridge (Logos)',
        'Transport/integrity foundations (LTP)',
        'Closed-source with public evidence',
    ]
    for i, item in enumerate(items_is):
        ax.text(0.7, 6.7 - i*0.65, f'{chr(8226)}  {item}', fontsize=10, va='top', color=COLORS['dark'])

    right = mpatches.FancyBboxPatch((6.6, 0.5), 5.0, 7.2, boxstyle="round,pad=0.2",
                                      facecolor=COLORS['red_fill'], edgecolor=COLORS['red'], linewidth=2.5)
    ax.add_patch(right)
    ax.text(9.1, 7.4, 'Sonata IS NOT', ha='center', va='bottom', fontsize=16, fontweight='bold', color=COLORS['red'])
    items_not = [
        'A finished product',
        'A commercially deployed service',
        'An open-source project',
        'A general-purpose AI system',
        'A mature reasoning platform',
        'A production-ready security system',
        'Guaranteed to scale beyond lab',
        'Ready for near-term deployment',
    ]
    for i, item in enumerate(items_not):
        ax.text(6.9, 6.7 - i*0.75, f'{chr(215)}  {item}', fontsize=10, va='top', color=COLORS['dark'])

    ax.set_title('Project Boundary', fontsize=18, fontweight='bold', pad=14, color=COLORS['dark'])
    path = os.path.join(OUTPUT, 'diagrams', 'project_boundary.png')
    save(path)

def diagram_public_private():
    fig, ax = plt.subplots(figsize=(11, 6.5))
    ax.set_xlim(0, 14); ax.set_ylim(0, 7.5)
    ax.axis('off')

    priv = mpatches.FancyBboxPatch((0.4, 0.4), 5.8, 6.2, boxstyle="round,pad=0.15",
                                    facecolor=COLORS['red_fill'], edgecolor=COLORS['red'], linewidth=2.5)
    ax.add_patch(priv)
    ax.text(3.3, 6.3, 'PRIVATE', ha='center', va='bottom', fontsize=15, fontweight='bold', color=COLORS['red'])
    ax.text(3.3, 5.9, 'Internal repository only', ha='center', va='bottom', fontsize=10, color=COLORS['grey'])
    priv_items = [
        'Full source code (Pascal, ASM, CUDA)',
        'Exact architectural recipes',
        'Experimental history & failures',
        'Raw training logs & checkpoints',
        'Future roadmap & research directions',
        'Internal documentation',
    ]
    for i, item in enumerate(priv_items):
        ax.text(0.7, 5.2 - i*0.65, f'{chr(9632)}  {item}', fontsize=10, va='top', color=COLORS['dark'])

    pub = mpatches.FancyBboxPatch((7.8, 0.4), 5.8, 6.2, boxstyle="round,pad=0.15",
                                    facecolor=COLORS['green_fill'], edgecolor=COLORS['green'], linewidth=2.5)
    ax.add_patch(pub)
    ax.text(10.7, 6.3, 'PUBLIC DOSSIER', ha='center', va='bottom', fontsize=15, fontweight='bold', color=COLORS['green'])
    ax.text(10.7, 5.9, 'This technical dossier', ha='center', va='bottom', fontsize=10, color=COLORS['grey'])
    pub_items = [
        'High-level architecture descriptions',
        'Selected benchmark metrics',
        'Verified capability summaries',
        'Validation test results',
        'Limitation & failure analyses',
        'Evidence index with references',
    ]
    for i, item in enumerate(pub_items):
        ax.text(8.1, 5.2 - i*0.65, f'{chr(9632)}  {item}', fontsize=10, va='top', color=COLORS['dark'])

    ax.annotate('', xy=(7.6, 3.5), xytext=(6.5, 3.5),
                arrowprops=dict(arrowstyle='->', color=COLORS['grey'], lw=2))
    ax.text(7.05, 3.9, 'curated\nextract', ha='center', va='bottom', fontsize=9, color=COLORS['grey'], style='italic')

    ax.set_title('Public / Private Disclosure Boundary', fontsize=18, fontweight='bold', pad=14, color=COLORS['dark'])
    path = os.path.join(OUTPUT, 'diagrams', 'public_private_boundary.png')
    save(path)

def diagram_layered_architecture():
    fig, ax = plt.subplots(figsize=(8, 9))
    ax.set_xlim(0, 8); ax.set_ylim(0, 11)
    ax.axis('off')

    layers = [
        ('Training & Inference\nExperiments', COLORS['purple'], COLORS['purple_fill'], 9.2),
        ('Symbolic Control\n(Logos Bridge)', COLORS['blue'], COLORS['blue_fill'], 7.7),
        ('Model & Checkpoint\nSystem', COLORS['green'], COLORS['green_fill'], 6.2),
        ('Tensor / Autograd\nEngine', COLORS['orange'], COLORS['orange_fill'], 4.7),
        ('Hardware Abstraction\nLayer (HAL)', COLORS['red'], COLORS['red_fill'], 3.2),
        ('Runtime\n(Memory, Dispatch, Thread Pool)', COLORS['dark'], COLORS['grey_fill'], 1.7),
    ]

    for label, edge_color, fill_color, y in layers:
        box = mpatches.FancyBboxPatch((1.8, y), 4.4, 1.15, boxstyle="round,pad=0.1",
                                        facecolor=fill_color, edgecolor=edge_color, linewidth=2)
        ax.add_patch(box)
        ax.text(4, y+0.575, label, ha='center', va='center', fontsize=10, color=COLORS['dark'], fontweight='normal')

    ax.text(0.5, 8.7, 'Application', fontsize=9, color=COLORS['grey'], rotation=90, va='center', fontweight='normal')
    ax.text(0.5, 5.2, 'Core Engine', fontsize=9, color=COLORS['grey'], rotation=90, va='center', fontweight='normal')
    ax.text(0.5, 2.3, 'System', fontsize=9, color=COLORS['grey'], rotation=90, va='center', fontweight='normal')

    for y_start, y_end in [(9.2, 7.7+1.15), (6.2, 4.7+1.15), (3.2, 1.7+1.15)]:
        ax.annotate('', xy=(4, y_end+0.05), xytext=(4, y_start-0.05),
                    arrowprops=dict(arrowstyle='->', color=COLORS['grey'], lw=1.2, connectionstyle='arc3,rad=0'))

    ax.set_title('Layered Architecture', fontsize=18, fontweight='bold', pad=14, color=COLORS['dark'])
    path = os.path.join(OUTPUT, 'diagrams', 'layered_architecture.png')
    save(path)

def diagram_backend_ladder():
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.set_xlim(0, 7); ax.set_ylim(0, 8)
    ax.axis('off')

    backends = [
        ('GPU (CUDA)\ncuBLAS + Custom Kernels', COLORS['green'], COLORS['green_fill'], 6.2),
        ('Multithreaded CPU\nPascal Thread Pool', COLORS['blue'], COLORS['blue_fill'], 4.5),
        ('Assembly (x86-64)\nSIMD Optimized Kernels', COLORS['orange'], COLORS['orange_fill'], 2.8),
        ('Pascal Reference\nUnoptimized Fallback', COLORS['red'], COLORS['red_fill'], 1.1),
    ]

    for label, edge_color, fill_color, y in backends:
        box = mpatches.FancyBboxPatch((1.0, y), 5.0, 1.3, boxstyle="round,pad=0.1",
                                        facecolor=fill_color, edgecolor=edge_color, linewidth=2)
        ax.add_patch(box)
        ax.text(3.5, y+0.65, label, ha='center', va='center', fontsize=10, color=COLORS['dark'], fontweight='normal')

    for y in [5.5, 3.8, 2.1]:
        ax.annotate('', xy=(3.5, y-0.1), xytext=(3.5, y+0.1),
                    arrowprops=dict(arrowstyle='->', color=COLORS['grey'], lw=1.5))

    ax.text(0.4, 4.5, 'Priority', fontsize=9, color=COLORS['grey'], rotation=90, va='center', fontweight='normal')
    ax.set_title('Backend Dispatch Chain', fontsize=18, fontweight='bold', pad=14, color=COLORS['dark'])
    path = os.path.join(OUTPUT, 'diagrams', 'backend_ladder.png')
    save(path)

def diagram_logos_control_loop():
    fig, ax = plt.subplots(figsize=(9, 6.5))
    ax.set_xlim(0, 12); ax.set_ylim(0, 8)
    ax.axis('off')

    neural = mpatches.FancyBboxPatch((0.5, 1.2), 4.2, 5.5, boxstyle="round,pad=0.15",
                                       facecolor=COLORS['blue_fill'], edgecolor=COLORS['blue'], linewidth=2.5)
    ax.add_patch(neural)
    ax.text(2.6, 6.4, 'Neural Stack', ha='center', fontsize=14, fontweight='bold', color=COLORS['blue'])
    ax.text(2.6, 5.9, 'Training / Inference', ha='center', fontsize=10, color=COLORS['grey'])
    items_n = ['Forward pass', 'Backward pass', 'Loss computation', 'Weight update']
    for i, item in enumerate(items_n):
        ax.text(0.9, 5.2 - i*0.7, f'{chr(8226)} {item}', fontsize=10.5, va='top', color=COLORS['dark'])

    logos = mpatches.FancyBboxPatch((7.3, 1.2), 4.2, 5.5, boxstyle="round,pad=0.15",
                                      facecolor=COLORS['green_fill'], edgecolor=COLORS['green'], linewidth=2.5)
    ax.add_patch(logos)
    ax.text(9.4, 6.4, 'Logos', ha='center', fontsize=14, fontweight='bold', color=COLORS['green'])
    ax.text(9.4, 5.9, 'Symbolic Control', ha='center', fontsize=10, color=COLORS['grey'])
    items_l = ['Contradiction detection', 'Axiom-guided penalties', 'Guarded evolution', 'Constraint validation']
    for i, item in enumerate(items_l):
        ax.text(7.7, 5.2 - i*0.7, f'{chr(8226)} {item}', fontsize=10.5, va='top', color=COLORS['dark'])

    ax.annotate('', xy=(7.15, 4.0), xytext=(4.85, 4.0),
                arrowprops=dict(arrowstyle='->', color=COLORS['grey'], lw=2))
    ax.annotate('', xy=(4.85, 2.8), xytext=(7.15, 2.8),
                arrowprops=dict(arrowstyle='->', color=COLORS['grey'], lw=2))
    ax.text(6.0, 4.4, 'outputs', ha='center', fontsize=9, color=COLORS['grey'], style='italic')
    ax.text(6.0, 2.3, 'penalties /\nconstraints', ha='center', fontsize=9, color=COLORS['grey'], style='italic')

    ax.set_title('Logos Neural / Symbolic Control Loop', fontsize=18, fontweight='bold', pad=14, color=COLORS['dark'])
    path = os.path.join(OUTPUT, 'diagrams', 'logos_control_loop.png')
    save(path)

def diagram_hardware_constraint():
    fig, ax = plt.subplots(figsize=(10, 5.5))
    ax.set_xlim(0, 12); ax.set_ylim(0, 6)
    ax.axis('off')

    constraints = [
        ('GPU', 'RTX 2070 Super\n(mobile, 8 GB)', COLORS['red'], COLORS['red_fill']),
        ('VRAM', '8 GB hard limit\nblocks large batches', COLORS['orange'], COLORS['orange_fill']),
        ('Thermals', 'Laptop cooling\nlimits sustained compute', COLORS['orange'], COLORS['orange_fill']),
        ('CPU', 'Intel i7-10750H\n6 cores / 12 threads', COLORS['blue'], COLORS['blue_fill']),
        ('RAM', '32 GB\nsufficient for lab work', COLORS['green'], COLORS['green_fill']),
    ]

    box_w = 2.0
    gap = 0.3
    start_x = 0.5
    for i, (label, desc, color, fill) in enumerate(constraints):
        x = start_x + i * (box_w + gap)
        box = mpatches.FancyBboxPatch((x, 1.0), box_w, 3.0, boxstyle="round,pad=0.12",
                                        facecolor=fill, edgecolor=color, linewidth=2.5)
        ax.add_patch(box)
        ax.text(x + box_w/2, 3.7, label, ha='center', va='bottom', fontsize=13, fontweight='bold', color=color)
        ax.text(x + box_w/2, 2.5, desc, ha='center', va='center', fontsize=9.5, color=COLORS['dark'])

    ax.set_title('Hardware Constraint Context', fontsize=18, fontweight='bold', pad=14, color=COLORS['dark'])
    path = os.path.join(OUTPUT, 'diagrams', 'hardware_constraint_panel.png')
    save(path)

# ─── PLOTS ────────────────────────────────────────────────────

def plot_stability_throughput():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.5))

    stages = ['task-87\nBaseline', 'Phase 20\nPre-fix', 'Phase 20\nPost-fix', 'Phase 20\nAMP v2']
    throughput = [2000, 7676, 5659, 5753]
    colors = [COLORS['grey'], COLORS['red'], COLORS['green'], COLORS['green']]

    bars = ax1.bar(stages, throughput, color=colors, width=0.55, edgecolor='white', linewidth=1.2)
    for bar, val in zip(bars, throughput):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 150,
                f'{val}', ha='center', va='bottom', fontsize=9, fontweight='bold', color=COLORS['dark'])

    ax1.set_ylabel('Throughput (tokens/sec)', fontweight='normal')
    ax1.set_title('Historical: Phase 20 Benchmark Correction', fontsize=11, fontweight='bold', color=COLORS['dark'])
    ax1.set_ylim(0, 9500)
    ax1.grid(True, axis='y', alpha=0.25)
    ax1.annotate('Memory leaks +\nVRAM overflow',
                xy=(1, 7676), xytext=(1.8, 8800),
                arrowprops=dict(arrowstyle='->', color=COLORS['red'], lw=1.5),
                fontsize=9, color=COLORS['red'], ha='center', fontweight='normal')

    stages2 = ['Sustained\n(Batch=8)', 'Peak Micro-benchmark\n(Batch=320)']
    throughput2 = [6802, 18172]
    colors2 = [COLORS['green'], COLORS['purple']]

    bars = ax2.bar(stages2, throughput2, color=colors2, width=0.45, edgecolor='white', linewidth=1.2)
    for bar, val in zip(bars, throughput2):
        label = f'{val} tok/s\n(overall)' if val < 10000 else f'{val} tok/s\n(4-step peak)'
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 300,
                label, ha='center', va='bottom', fontsize=9, fontweight='bold', color=COLORS['dark'])

    ax2.set_ylabel('Throughput (tokens/sec)', fontweight='normal')
    ax2.set_title('Current: TinyStories BPE Training', fontsize=11, fontweight='bold', color=COLORS['dark'])
    ax2.set_ylim(0, 23000)
    ax2.grid(True, axis='y', alpha=0.25)
    ax2.text(0.5, 800, 'Model: 2-layer Mamba LM, 182K params\nSeqLen=128, ActiveVocab=73\nSustained: 30 steps, profile-default',
             ha='center', fontsize=8.5, color=COLORS['grey'], style='italic')

    fig.suptitle('Training Throughput: Historical Correction and Current Results',
                 fontsize=15, fontweight='bold', y=1.02, color=COLORS['dark'])
    fig.tight_layout()
    path = os.path.join(OUTPUT, 'plots', 'stability_throughput.png')
    save(path, fig)

def plot_int8_validation():
    fig, axes = plt.subplots(1, 2, figsize=(11, 5))

    tests = ['MatMul\nCorrectness', 'GPU\nDispatch', 'GPUvsCPU\nParity', 'Serialization\nRound-Trip', 'Large Matrix\nStress']
    mse_values = [0.000013, 0.000035, 0.000495, 0.000002, 0.000220]
    thresholds = [0.01, 0.01, 0.001, 0.01, 0.05]

    ax = axes[0]
    x = np.arange(len(tests))
    width = 0.32
    bars1 = ax.bar(x - width/2, mse_values, width, label='Measured MSE', color=COLORS['blue'], edgecolor='white', linewidth=1)
    bars2 = ax.bar(x + width/2, thresholds, width, label='Threshold', color=COLORS['red'], alpha=0.5, edgecolor='white', linewidth=1)
    ax.set_ylabel('MSE (lower is better)', fontweight='normal')
    ax.set_title('INT8 Numerical Fidelity', fontsize=11, fontweight='bold', color=COLORS['dark'])
    ax.set_xticks(x)
    ax.set_xticklabels(tests, fontsize=8.5)
    ax.legend(fontsize=9, framealpha=0.9)
    ax.grid(True, axis='y', alpha=0.25)
    ax.set_yscale('log')

    ax = axes[1]
    categories = ['Weights\nMemory', 'FP32\nBatch=4', 'INT8\nBatch=8']
    values = [2.1, 5750, 10832]
    labels = ['2.1x\nsmaller', '5750\ntok/s', '10832\ntok/s']
    colors = [COLORS['green'], COLORS['orange'], COLORS['blue']]

    bars = ax.bar(categories, values, color=colors, width=0.5, edgecolor='white', linewidth=1.2)
    for bar, val, label in zip(bars, values, labels):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 250,
                label, ha='center', va='bottom', fontsize=9, fontweight='bold', color=COLORS['dark'])
    ax.set_ylabel('Memory Compression / Throughput', fontweight='normal')
    ax.set_title('INT8 Memory & Speed Impact', fontsize=11, fontweight='bold', color=COLORS['dark'])
    ax.grid(True, axis='y', alpha=0.25)

    fig.suptitle('INT8 Quantization Validation', fontsize=15, fontweight='bold', y=1.02, color=COLORS['dark'])
    fig.tight_layout()
    path = os.path.join(OUTPUT, 'plots', 'int8_validation.png')
    save(path, fig)

def plot_throughput_comparison():
    fig, ax = plt.subplots(figsize=(7, 5))

    configs = ['Sustained\n(Batch=8, 30 steps)', 'Peak Micro-benchmark\n(Batch=320)', 'Phase 20\n(ref, Batch=4)']
    values = [6802, 18172, 5659]
    colors = [COLORS['green'], COLORS['purple'], COLORS['orange']]

    bars = ax.bar(configs, values, color=colors, width=0.5, edgecolor='white', linewidth=1.2)
    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 300,
                f'{val} tok/s', ha='center', va='bottom', fontsize=10, fontweight='bold', color=COLORS['dark'])

    ax.set_ylabel('Throughput (tokens/sec)', fontweight='normal')
    ax.set_title('Training Throughput: Sustained vs Peak vs Historical', fontsize=12, fontweight='bold', color=COLORS['dark'])
    ax.set_ylim(0, 23000)
    ax.grid(True, axis='y', alpha=0.25)

    ax.text(0.5, 800, 'TinyStories BPE, 2-layer Mamba LM  |  GPU: RTX 2070 Super 8GB',
             ha='center', fontsize=9, color=COLORS['grey'], style='italic')

    path = os.path.join(OUTPUT, 'plots', 'throughput_comparison.png')
    save(path)

def plot_vram_usage():
    fig, ax = plt.subplots(figsize=(8, 5))

    categories = ['Model\nWeights', 'Activations\n& Autograd', 'Cached\nPool', 'Free']
    values_sustained = [0.05, 1.0, 0.15, 6.8]
    values_peak = [0.05, 2.95, 4.5, 0.5]

    x = [0, 0.7]
    bar_width = 0.4
    colors_vram = [COLORS['green'], COLORS['blue'], COLORS['orange'], COLORS['grey']+'60']

    bottoms = [0]
    for i, (val, color) in enumerate(zip(values_sustained, colors_vram)):
        ax.bar(x[0], val, width=bar_width, bottom=sum(values_sustained[:i]),
               color=color, edgecolor='white', linewidth=0.8, label=categories[i] if i == 0 else '')
        if val > 0.3:
            mid = sum(values_sustained[:i]) + val/2
            ax.text(x[0], mid, f'{val} GB', ha='center', va='center', fontsize=8.5, color='white', fontweight='bold')

    for i, (val, color) in enumerate(zip(values_peak, colors_vram)):
        ax.bar(x[1], val, width=bar_width, bottom=sum(values_peak[:i]),
               color=color, edgecolor='white', linewidth=0.8)
        if val > 0.3:
            mid = sum(values_peak[:i]) + val/2
            ax.text(x[1], mid, f'{val} GB', ha='center', va='center', fontsize=8.5, color='white', fontweight='bold')

    ax.set_xticks(x)
    ax.set_xticklabels(['Sustained\n(Batch=8, 30 steps)', 'Peak\n(Batch=320, 4 steps)'], fontsize=10)
    ax.set_ylabel('VRAM (GB)', fontweight='normal')
    ax.set_title('VRAM Usage: Sustained Training vs Peak Micro-Benchmark', fontsize=12, fontweight='bold', color=COLORS['dark'])
    ax.set_ylim(0, 9.0)
    ax.axhline(y=8, color=COLORS['red'], linestyle='--', linewidth=1.2, alpha=0.7)
    ax.text(0.85, 8.15, '8 GB limit', fontsize=9, color=COLORS['red'], va='bottom', fontweight='normal')
    ax.legend(loc='upper left', fontsize=9, framealpha=0.9)
    ax.grid(True, axis='y', alpha=0.25)

    path = os.path.join(OUTPUT, 'plots', 'vram_usage.png')
    save(path)

def plot_h2d_traffic():
    fig, ax = plt.subplots(figsize=(7, 5))

    stages = ['Baseline\n(task-87)', 'Phase 20\nPost-fix', 'TinyStories\nSustained\n(Batch=8)', 'TinyStories\nPeak\n(Batch=320)']
    traffic = [2048, 16, 5.2, 407.9]
    colors_h2d = [COLORS['red'], COLORS['green'], COLORS['blue'], COLORS['purple']]

    bars = ax.bar(stages, traffic, color=colors_h2d, width=0.45, edgecolor='white', linewidth=1.2)
    for bar, val in zip(bars, traffic):
        if val > 100:
            label = f'{int(val)} MB'
        elif val > 1:
            label = f'{val} MB'
        else:
            label = f'{val} KB'
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() * 1.15,
                label, ha='center', va='bottom', fontsize=9, fontweight='bold', color=COLORS['dark'])

    ax.set_ylabel('H2D Traffic per Run', fontweight='normal')
    ax.set_title('Host-to-Device Traffic by Configuration', fontsize=12, fontweight='bold', color=COLORS['dark'])
    ax.set_yscale('log')
    ax.grid(True, axis='y', alpha=0.25)

    ax.annotate('Sustained: 124 copies\nPeak: 1228 copies\n(30x more steps)',
                xy=(3, 407.9), xytext=(2.2, 1200),
                arrowprops=dict(arrowstyle='->', color=COLORS['purple'], lw=1.5),
                fontsize=9, color=COLORS['purple'], ha='center',
                bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor=COLORS['purple'], alpha=0.9))

    path = os.path.join(OUTPUT, 'plots', 'h2d_traffic_reduction.png')
    save(path)

def plot_autograd_mamba_flow():
    fig, ax = plt.subplots(figsize=(11, 4.5))
    ax.set_xlim(0, 14); ax.set_ylim(0, 5)
    ax.axis('off')

    boxes = [
        ('Input\nTokens', 0.5, COLORS['grey'], COLORS['grey_fill']),
        ('Embedding', 2.7, COLORS['blue'], COLORS['blue_fill']),
        ('Mamba\nSSM Layer', 5.2, COLORS['purple'], COLORS['purple_fill']),
        ('Output\nProjection', 7.7, COLORS['orange'], COLORS['orange_fill']),
        ('Loss\n(Cross-Entropy)', 10.2, COLORS['red'], COLORS['red_fill']),
        ('Backward\nPass', 12.2, COLORS['green'], COLORS['green_fill']),
    ]

    box_w = 1.8
    box_h = 1.4
    box_y = 1.8
    for label, x, color, fill in boxes:
        box = mpatches.FancyBboxPatch((x, box_y), box_w, box_h, boxstyle="round,pad=0.08",
                                        facecolor=fill, edgecolor=color, linewidth=2)
        ax.add_patch(box)
        ax.text(x + box_w/2, box_y + box_h/2, label, ha='center', va='center', fontsize=9.5, color=COLORS['dark'], fontweight='normal')

    for x_start in [0.5, 2.7, 5.2, 7.7, 10.2]:
        ax.annotate('', xy=(x_start + box_w + 0.15, box_y + box_h/2), xytext=(x_start + box_w - 0.15, box_y + box_h/2),
                    arrowprops=dict(arrowstyle='->', color=COLORS['dark'], lw=1.5))

    ax.annotate('Gradient flow (backward)', xy=(5.0, 1.0), xytext=(5.0, 1.8),
                arrowprops=dict(arrowstyle='->', color=COLORS['green'], lw=1.5),
                fontsize=9, color=COLORS['green'], ha='center', fontweight='normal')

    ax.set_title('Training Flow: Autograd + Mamba Integration', fontsize=15, fontweight='bold', pad=14, color=COLORS['dark'])
    path = os.path.join(OUTPUT, 'diagrams', 'autograd_mamba_flow.png')
    save(path)

def plot_benchmark_timeline():
    fig, ax = plt.subplots(figsize=(10, 3.5))
    ax.set_xlim(0, 12); ax.set_ylim(0, 3)
    ax.axis('off')

    events = [
        (1.0, 'task-87\n~2000 tok/s', COLORS['grey']),
        (3.2, 'Phase 20\n(pre-fix)\n~7676 tok/s', COLORS['red']),
        (5.6, 'Memory leak\ndiscovered', COLORS['orange']),
        (7.8, 'Safety fuse\nimplemented', COLORS['orange']),
        (10.2, 'Phase 20\n(post-fix)\n~5659 tok/s', COLORS['green']),
    ]

    ax.plot([1.0, 10.2], [1.8, 1.8], '-', color=COLORS['grey'], lw=2.5, zorder=1)
    for x, label, color in events:
        ax.plot(x, 1.8, 'o', color=color, markersize=18, zorder=2, markeredgecolor='white', markeredgewidth=2)
        ax.text(x, 0.4, label, ha='center', va='top', fontsize=9.5, color=COLORS['dark'], fontweight='normal')

    ax.set_title('Benchmark Timeline: Instability to Stability', fontsize=15, fontweight='bold', pad=14, color=COLORS['dark'])
    path = os.path.join(OUTPUT, 'diagrams', 'benchmark_timeline.png')
    save(path)

# ─── MAIN ─────────────────────────────────────────────────────

def main():
    print("Generating diagrams...")
    diagram_project_boundary()
    diagram_public_private()
    diagram_layered_architecture()
    diagram_backend_ladder()
    diagram_logos_control_loop()
    diagram_hardware_constraint()
    plot_autograd_mamba_flow()
    plot_benchmark_timeline()

    print("Generating plots...")
    plot_stability_throughput()
    plot_int8_validation()
    plot_throughput_comparison()
    plot_vram_usage()
    plot_h2d_traffic()

    print("Generating thumbnails...")
    for root, dirs, files in os.walk(os.path.join(OUTPUT, 'diagrams')):
        for f in files:
            if f.endswith('.png'):
                thumbnail(os.path.join(root, f))
    for root, dirs, files in os.walk(os.path.join(OUTPUT, 'plots')):
        for f in files:
            if f.endswith('.png'):
                thumbnail(os.path.join(root, f))

    print("Done. All assets generated.")

if __name__ == '__main__':
    main()
