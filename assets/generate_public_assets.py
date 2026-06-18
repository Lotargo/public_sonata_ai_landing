import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

OUTPUT = os.path.dirname(os.path.abspath(__file__))

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'figure.dpi': 150,
    'savefig.dpi': 150,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.15,
})

COLORS = {
    'blue': '#4A90D9',
    'green': '#50B86C',
    'red': '#E06060',
    'orange': '#E8A040',
    'purple': '#9060C8',
    'grey': '#808080',
    'light_grey': '#E8E8E8',
    'dark': '#2C3E50',
    'white': '#FAFAFA',
}

def save(path, fig=None):
    if fig is None:
        fig = plt.gcf()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fig.savefig(path)
    plt.close(fig)
    print(f"  Saved: {os.path.relpath(path, OUTPUT)}")

def thumbnail(src_path):
    thumb_dir = os.path.join(OUTPUT, 'thumbnails')
    os.makedirs(thumb_dir, exist_ok=True)
    name = os.path.basename(src_path)
    thumb_path = os.path.join(thumb_dir, name)
    from PIL import Image
    img = Image.open(src_path)
    img.thumbnail((320, 240), Image.LANCZOS)
    img.save(thumb_path)
    print(f"  Thumbnail: {os.path.relpath(thumb_path, OUTPUT)}")

# ─── DIAGRAMS ────────────────────────────────────────────────

def diagram_project_boundary():
    fig, ax = plt.subplots(figsize=(8, 5.5))
    ax.set_xlim(0, 10); ax.set_ylim(0, 7)
    ax.axis('off')

    # Left: IS
    left = mpatches.FancyBboxPatch((0.3, 0.5), 4.2, 6, boxstyle="round,pad=0.15",
                                     facecolor=COLORS['blue']+'30', edgecolor=COLORS['blue'], linewidth=2)
    ax.add_patch(left)
    ax.text(2.4, 6.2, 'Sonata IS', ha='center', va='bottom', fontsize=14, fontweight='bold', color=COLORS['blue'])
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
        ax.text(0.6, 5.6 - i*0.55, f'  {chr(8226)}  {item}', fontsize=8.5, va='top', color=COLORS['dark'])

    # Right: IS NOT
    right = mpatches.FancyBboxPatch((5.5, 0.5), 4.2, 6, boxstyle="round,pad=0.15",
                                      facecolor=COLORS['red']+'20', edgecolor=COLORS['red'], linewidth=2)
    ax.add_patch(right)
    ax.text(7.6, 6.2, 'Sonata IS NOT', ha='center', va='bottom', fontsize=14, fontweight='bold', color=COLORS['red'])
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
        ax.text(5.8, 5.6 - i*0.6, f'  {chr(215)}  {item}', fontsize=8.5, va='top', color=COLORS['dark'])

    ax.set_title('Project Boundary', fontsize=15, fontweight='bold', pad=10)
    path = os.path.join(OUTPUT, 'diagrams', 'project_boundary.png')
    save(path)

def diagram_public_private():
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.set_xlim(0, 12); ax.set_ylim(0, 6)
    ax.axis('off')

    # Private side
    priv = mpatches.FancyBboxPatch((0.3, 0.4), 5.2, 5.2, boxstyle="round,pad=0.12",
                                    facecolor=COLORS['red']+'20', edgecolor=COLORS['red'], linewidth=2)
    ax.add_patch(priv)
    ax.text(2.9, 5.3, 'PRIVATE', ha='center', va='bottom', fontsize=13, fontweight='bold', color=COLORS['red'])
    ax.text(2.9, 4.9, 'Internal repository only', ha='center', va='bottom', fontsize=9, color=COLORS['grey'])
    priv_items = [
        'Full source code (Pascal, ASM, CUDA)',
        'Exact architectural recipes',
        'Experimental history & failures',
        'Raw training logs & checkpoints',
        'Future roadmap & research directions',
        'Internal documentation',
    ]
    for i, item in enumerate(priv_items):
        ax.text(0.6, 4.3 - i*0.55, f'  {chr(9632)}  {item}', fontsize=8.5, va='top', color=COLORS['dark'])

    # Public side
    pub = mpatches.FancyBboxPatch((6.5, 0.4), 5.2, 5.2, boxstyle="round,pad=0.12",
                                    facecolor=COLORS['green']+'20', edgecolor=COLORS['green'], linewidth=2)
    ax.add_patch(pub)
    ax.text(9.1, 5.3, 'PUBLIC DOSSIER', ha='center', va='bottom', fontsize=13, fontweight='bold', color=COLORS['green'])
    ax.text(9.1, 4.9, 'This technical dossier', ha='center', va='bottom', fontsize=9, color=COLORS['grey'])
    pub_items = [
        'High-level architecture descriptions',
        'Selected benchmark metrics',
        'Verified capability summaries',
        'Validation test results',
        'Limitation & failure analyses',
        'Evidence index with references',
    ]
    for i, item in enumerate(pub_items):
        ax.text(6.8, 4.3 - i*0.55, f'  {chr(9632)}  {item}', fontsize=8.5, va='top', color=COLORS['dark'])

    # Arrow between
    ax.annotate('', xy=(6.4, 2.8), xytext=(5.6, 2.8),
                arrowprops=dict(arrowstyle='->', color=COLORS['grey'], lw=1.5))
    ax.text(6.0, 3.1, 'curated\nextract', ha='center', va='bottom', fontsize=8, color=COLORS['grey'])

    ax.set_title('Public / Private Disclosure Boundary', fontsize=15, fontweight='bold', pad=10)
    path = os.path.join(OUTPUT, 'diagrams', 'public_private_boundary.png')
    save(path)

def diagram_layered_architecture():
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.set_xlim(0, 8); ax.set_ylim(0, 10)
    ax.axis('off')

    layers = [
        ('Training & Inference\nExperiments', COLORS['purple'], 8.3),
        ('Symbolic Control\n(Logos Bridge)', COLORS['blue'], 6.9),
        ('Model & Checkpoint\nSystem', COLORS['green'], 5.5),
        ('Tensor / Autograd\nEngine', COLORS['orange'], 4.1),
        ('Hardware Abstraction\nLayer (HAL)', COLORS['red'], 2.7),
        ('Runtime\n(Memory, Dispatch, Thread Pool)', COLORS['dark'], 1.3),
    ]

    for label, color, y in layers:
        box = mpatches.FancyBboxPatch((1.5, y), 5, 0.9, boxstyle="round,pad=0.08",
                                        facecolor=color+'30', edgecolor=color, linewidth=1.5)
        ax.add_patch(box)
        ax.text(4, y+0.45, label, ha='center', va='center', fontsize=9, color=COLORS['dark'])

    # Side labels
    ax.text(0.3, 7.6, 'Application', fontsize=8, color=COLORS['grey'], rotation=90, va='center')
    ax.text(0.3, 4.1, 'Core Engine', fontsize=8, color=COLORS['grey'], rotation=90, va='center')
    ax.text(0.3, 1.9, 'System', fontsize=8, color=COLORS['grey'], rotation=90, va='center')

    ax.set_title('Layered Architecture', fontsize=15, fontweight='bold', pad=10)
    path = os.path.join(OUTPUT, 'diagrams', 'layered_architecture.png')
    save(path)

def diagram_backend_ladder():
    fig, ax = plt.subplots(figsize=(6, 5.5))
    ax.set_xlim(0, 6); ax.set_ylim(0, 6)
    ax.axis('off')

    backends = [
        ('GPU (CUDA)\ncuBLAS + Custom Kernels', COLORS['green'], 4.8),
        ('Multithreaded CPU\nPascal Thread Pool', COLORS['blue'], 3.4),
        ('Assembly (x86-64)\nSIMD Optimized Kernels', COLORS['orange'], 2.0),
        ('Pascal Reference\nUnoptimized Fallback', COLORS['red'], 0.6),
    ]

    for label, color, y in backends:
        box = mpatches.FancyBboxPatch((0.8, y), 4.4, 1.0, boxstyle="round,pad=0.08",
                                        facecolor=color+'25', edgecolor=color, linewidth=1.5)
        ax.add_patch(box)
        ax.text(3.0, y+0.5, label, ha='center', va='center', fontsize=9, color=COLORS['dark'])

    # Arrows
    for y in [4.2, 2.8, 1.4]:
        ax.annotate('', xy=(3.0, y-0.2), xytext=(3.0, y+0.2),
                    arrowprops=dict(arrowstyle='->', color=COLORS['grey'], lw=1))

    ax.text(0.2, 2.7, 'Priority', fontsize=8, color=COLORS['grey'], rotation=90, va='center')
    ax.set_title('Backend Dispatch Chain', fontsize=15, fontweight='bold', pad=10)
    path = os.path.join(OUTPUT, 'diagrams', 'backend_ladder.png')
    save(path)

def diagram_logos_control_loop():
    fig, ax = plt.subplots(figsize=(7, 5.5))
    ax.set_xlim(0, 10); ax.set_ylim(0, 7)
    ax.axis('off')

    # Neural stack
    neural = mpatches.FancyBboxPatch((0.5, 1.5), 3.5, 4, boxstyle="round,pad=0.12",
                                       facecolor=COLORS['blue']+'20', edgecolor=COLORS['blue'], linewidth=2)
    ax.add_patch(neural)
    ax.text(2.25, 5.2, 'Neural Stack', ha='center', fontsize=12, fontweight='bold', color=COLORS['blue'])
    ax.text(2.25, 4.7, 'Training / Inference', ha='center', fontsize=9, color=COLORS['grey'])
    items_n = ['Forward pass', 'Backward pass', 'Loss computation', 'Weight update']
    for i, item in enumerate(items_n):
        ax.text(0.8, 4.0 - i*0.55, f'  {chr(8226)} {item}', fontsize=8.5, va='top', color=COLORS['dark'])

    # Logos
    logos = mpatches.FancyBboxPatch((6, 1.5), 3.5, 4, boxstyle="round,pad=0.12",
                                      facecolor=COLORS['green']+'20', edgecolor=COLORS['green'], linewidth=2)
    ax.add_patch(logos)
    ax.text(7.75, 5.2, 'Logos', ha='center', fontsize=12, fontweight='bold', color=COLORS['green'])
    ax.text(7.75, 4.7, 'Symbolic Control', ha='center', fontsize=9, color=COLORS['grey'])
    items_l = ['Contradiction detection', 'Axiom-guided penalties', 'Guarded evolution', 'Constraint validation']
    for i, item in enumerate(items_l):
        ax.text(6.3, 4.0 - i*0.55, f'  {chr(8226)} {item}', fontsize=8.5, va='top', color=COLORS['dark'])

    # Arrows
    ax.annotate('', xy=(5.9, 3.5), xytext=(4.1, 3.5),
                arrowprops=dict(arrowstyle='->', color=COLORS['grey'], lw=1.5))
    ax.annotate('', xy=(4.1, 2.5), xytext=(5.9, 2.5),
                arrowprops=dict(arrowstyle='->', color=COLORS['grey'], lw=1.5))
    ax.text(5.0, 3.8, 'outputs', ha='center', fontsize=8, color=COLORS['grey'])
    ax.text(5.0, 2.2, 'penalties /\nconstraints', ha='center', fontsize=8, color=COLORS['grey'])

    ax.set_title('Logos Neural / Symbolic Control Loop', fontsize=15, fontweight='bold', pad=10)
    path = os.path.join(OUTPUT, 'diagrams', 'logos_control_loop.png')
    save(path)

def diagram_hardware_constraint():
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.set_xlim(0, 8); ax.set_ylim(0, 5)
    ax.axis('off')

    constraints = [
        ('GPU', 'RTX 2070 Super\n(mobile, 8 GB VRAM)', COLORS['red']),
        ('VRAM', '8 GB hard limit\nblocks large batches', COLORS['orange']),
        ('Thermals', 'Laptop cooling\nlimits sustained compute', COLORS['orange']),
        ('CPU', 'Intel i7-10750H\n6 cores / 12 threads', COLORS['blue']),
        ('RAM', '32 GB\nsufficient for lab work', COLORS['green']),
    ]

    for i, (label, desc, color) in enumerate(constraints):
        x = 0.3 + i * 1.5
        box = mpatches.FancyBboxPatch((x, 0.5), 1.3, 1.8, boxstyle="round,pad=0.08",
                                        facecolor=color+'20', edgecolor=color, linewidth=1.5)
        ax.add_patch(box)
        ax.text(x+0.65, 2.1, label, ha='center', va='bottom', fontsize=10, fontweight='bold', color=color)
        ax.text(x+0.65, 1.3, desc, ha='center', va='center', fontsize=7.5, color=COLORS['dark'])

    ax.set_title('Hardware Constraint Context', fontsize=15, fontweight='bold', pad=10)
    path = os.path.join(OUTPUT, 'diagrams', 'hardware_constraint_panel.png')
    save(path)

# ─── PLOTS ────────────────────────────────────────────────────

def plot_stability_throughput():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5))

    # Left: historical correction story
    stages = ['task-87\nBaseline', 'Phase 20\nPre-fix', 'Phase 20\nPost-fix', 'Phase 20\nAMP v2']
    throughput = [2000, 7676, 5659, 5753]
    colors = [COLORS['grey'], COLORS['red'], COLORS['green'], COLORS['green']]

    bars = ax1.bar(stages, throughput, color=colors, width=0.5, edgecolor='white')
    for bar, val in zip(bars, throughput):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 100,
                f'{val}', ha='center', va='bottom', fontsize=7, fontweight='bold')

    ax1.set_ylabel('Throughput (tokens/sec)')
    ax1.set_title('Historical: Phase 20 Benchmark Correction')
    ax1.set_ylim(0, 9000)
    ax1.grid(True, axis='y', alpha=0.3)
    ax1.annotate('Memory leaks +\nVRAM overflow',
                xy=(1, 7676), xytext=(1.5, 8500),
                arrowprops=dict(arrowstyle='->', color=COLORS['red'], lw=1),
                fontsize=7, color=COLORS['red'], ha='center')

    # Right: current TinyStories results
    stages2 = ['Sustained\n(Batch=8)', 'Peak\n(Batch=320,\nmicro-benchmark)']
    throughput2 = [6802, 18172]
    colors2 = [COLORS['green'], COLORS['purple']]

    bars = ax2.bar(stages2, throughput2, color=colors2, width=0.4, edgecolor='white')
    for bar, val in zip(bars, throughput2):
        label = f'{val} tok/s'
        if val < 10000:
            label = f'~{val} tok/s\n(overall)'
        else:
            label = f'{val} tok/s\n(4-step peak)'
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 200,
                label, ha='center', va='bottom', fontsize=8, fontweight='bold')

    ax2.set_ylabel('Throughput (tokens/sec)')
    ax2.set_title('Current: TinyStories BPE Training')
    ax2.set_ylim(0, 22000)
    ax2.grid(True, axis='y', alpha=0.3)
    ax2.text(0.5, 500, 'Model: 2-layer Mamba LM, 182K params\nSeqLen=128, ActiveVocab=73',
             ha='center', fontsize=7, color=COLORS['grey'])
    ax2.text(0.5, 1500, 'Sustained: 30 steps, profile-default',
             ha='center', fontsize=7, color=COLORS['grey'])

    fig.suptitle('Training Throughput: Historical Correction and Current Results',
                 fontsize=13, fontweight='bold', y=1.02)
    fig.tight_layout()
    path = os.path.join(OUTPUT, 'plots', 'stability_throughput.png')
    save(path, fig)

def plot_int8_validation():
    fig, axes = plt.subplots(1, 2, figsize=(9, 4))

    # Left: MSE metrics
    tests = ['MatMul\nCorrectness', 'GPU Dispatch', 'GPUvsCPU\nParity', 'Serialization\nRound-Trip', 'Large Matrix\nStress']
    mse_values = [0.000013, 0.000035, 0.000495, 0.000002, 0.000220]
    thresholds = [0.01, 0.01, 0.001, 0.01, 0.05]

    ax = axes[0]
    x = np.arange(len(tests))
    width = 0.3
    bars1 = ax.bar(x - width/2, mse_values, width, label='Measured MSE', color=COLORS['blue'])
    bars2 = ax.bar(x + width/2, thresholds, width, label='Threshold', color=COLORS['red'], alpha=0.6)
    ax.set_ylabel('MSE (lower is better)')
    ax.set_title('INT8 Numerical Fidelity')
    ax.set_xticks(x)
    ax.set_xticklabels(tests, fontsize=7)
    ax.legend(fontsize=7)
    ax.grid(True, axis='y', alpha=0.3)
    ax.set_yscale('log')

    # Right: Memory & throughput
    ax = axes[1]
    categories = ['Weights\nMemory', 'FP32\nBatch=4', 'INT8\nBatch=8']
    values = [2.1, 5750, 10832]
    labels = ['2.1x\nsmaller', '5750\ntok/s', '10832\ntok/s']
    colors = [COLORS['green'], COLORS['orange'], COLORS['blue']]

    bars = ax.bar(categories, values, color=colors, width=0.5, edgecolor='white')
    for bar, val, label in zip(bars, values, labels):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 200,
                label, ha='center', va='bottom', fontsize=8, fontweight='bold')
    ax.set_ylabel('Memory Compression / Throughput')
    ax.set_title('INT8 Memory & Speed Impact')
    ax.grid(True, axis='y', alpha=0.3)

    fig.suptitle('INT8 Quantization Validation', fontsize=14, fontweight='bold', y=1.02)
    fig.tight_layout()
    path = os.path.join(OUTPUT, 'plots', 'int8_validation.png')
    save(path, fig)

def plot_throughput_comparison():
    fig, ax = plt.subplots(figsize=(6, 4))

    configs = ['Sustained\n(Batch=8, 30 steps)', 'Peak Micro-\nbenchmark\n(Batch=320)', 'Phase 20\n(ref, Batch=4)']
    values = [6802, 18172, 5659]
    colors = [COLORS['green'], COLORS['purple'], COLORS['orange']]

    bars = ax.bar(configs, values, color=colors, width=0.45, edgecolor='white')
    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 200,
                f'{val} tok/s', ha='center', va='bottom', fontsize=9, fontweight='bold')

    ax.set_ylabel('Throughput (tokens/sec)')
    ax.set_title('Training Throughput: Sustained vs Peak vs Historical')
    ax.set_ylim(0, 22000)
    ax.grid(True, axis='y', alpha=0.3)

    ax.text(1, 500, 'TinyStories BPE, 2-layer Mamba LM\nGPU: RTX 2070 Super 8GB',
             ha='center', fontsize=7.5, color=COLORS['grey'])

    path = os.path.join(OUTPUT, 'plots', 'throughput_comparison.png')
    save(path)

def plot_vram_usage():
    fig, ax = plt.subplots(figsize=(7, 4))

    categories = ['Model\nWeights', 'Activations\n& Autograd', 'Cached\nPool', 'Free']
    values_sustained = [0.05, 1.0, 0.15, 6.8]
    values_peak = [0.05, 2.95, 4.5, 0.5]

    x = [0, 0.6]
    bar_width = 0.35
    colors_vram = [COLORS['green'], COLORS['blue'], COLORS['orange'], COLORS['grey']+'40']

    # Sustained bar (stacked)
    bottoms = [0]
    for i, (val, color) in enumerate(zip(values_sustained, colors_vram)):
        ax.bar(x[0], val, width=bar_width, bottom=sum(values_sustained[:i]),
               color=color, edgecolor='white', label=categories[i] if i == 0 else '')
        if val > 0.3:
            mid = sum(values_sustained[:i]) + val/2
            ax.text(x[0], mid, f'{val} GB', ha='center', va='center', fontsize=7, color='white', fontweight='bold')

    # Peak bar (stacked)
    for i, (val, color) in enumerate(zip(values_peak, colors_vram)):
        ax.bar(x[1], val, width=bar_width, bottom=sum(values_peak[:i]),
               color=color, edgecolor='white')
        if val > 0.3:
            mid = sum(values_peak[:i]) + val/2
            ax.text(x[1], mid, f'{val} GB', ha='center', va='center', fontsize=7, color='white', fontweight='bold')

    ax.set_xticks(x)
    ax.set_xticklabels(['Sustained\n(Batch=8, 30 steps)', 'Peak\n(Batch=320, 4 steps)'])
    ax.set_ylabel('VRAM (GB)')
    ax.set_title('VRAM Usage: Sustained Training vs Peak Micro-Benchmark')
    ax.set_ylim(0, 8.5)
    ax.axhline(y=8, color=COLORS['red'], linestyle='--', linewidth=1, alpha=0.6)
    ax.text(0.8, 8.1, '8 GB limit', fontsize=8, color=COLORS['red'], va='bottom')
    ax.legend(loc='upper right', fontsize=7)
    ax.grid(True, axis='y', alpha=0.3)

    path = os.path.join(OUTPUT, 'plots', 'vram_usage.png')
    save(path)

def plot_h2d_traffic():
    fig, ax = plt.subplots(figsize=(6, 4))

    stages = ['Baseline\n(task-87)', 'Phase 20\nPost-fix', 'TinyStories\nSustained\n(Batch=8)', 'TinyStories\nPeak\n(Batch=320)']
    traffic = [2048, 16, 5.2, 407.9]
    colors_h2d = [COLORS['red'], COLORS['green'], COLORS['blue'], COLORS['purple']]

    bars = ax.bar(stages, traffic, color=colors_h2d, width=0.4, edgecolor='white')
    for bar, val in zip(bars, traffic):
        if val > 100:
            label = f'{int(val)} MB'
        elif val > 1:
            label = f'{val} MB'
        else:
            label = f'{val} KB'
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5,
                label, ha='center', va='bottom', fontsize=8, fontweight='bold')

    ax.set_ylabel('H2D Traffic per Run')
    ax.set_title('Host-to-Device Traffic by Configuration')
    ax.set_yscale('log')
    ax.grid(True, axis='y', alpha=0.3)

    ax.annotate('Sustained: 124 copies\nPeak: 1228 copies\n(30× more steps)',
                xy=(3, 407.9), xytext=(2.5, 800),
                arrowprops=dict(arrowstyle='->', color=COLORS['purple'], lw=1),
                fontsize=7, color=COLORS['purple'], ha='center')

    path = os.path.join(OUTPUT, 'plots', 'h2d_traffic_reduction.png')
    save(path)

def plot_autograd_mamba_flow():
    fig, ax = plt.subplots(figsize=(8, 3.5))
    ax.set_xlim(0, 10); ax.set_ylim(0, 3.5)
    ax.axis('off')

    boxes = [
        ('Input\nTokens', 0.3, COLORS['grey']),
        ('Embedding', 1.8, COLORS['blue']),
        ('Mamba\nSSM Layer', 3.8, COLORS['purple']),
        ('Output\nProjection', 5.8, COLORS['orange']),
        ('Loss\n(Cross-Entropy)', 7.8, COLORS['red']),
        ('Backward\nPass', 9.3, COLORS['green'], 'right'),
    ]

    for item in boxes:
        label, x, color = item[0], item[1], item[2]
        align = item[3] if len(item) > 3 else 'center'
        box = mpatches.FancyBboxPatch((x, 1.0), 1.2, 0.8, boxstyle="round,pad=0.06",
                                        facecolor=color+'25', edgecolor=color, linewidth=1.5)
        ax.add_patch(box)
        ax.text(x+0.6, 1.4, label, ha='center', va='center', fontsize=7.5, color=COLORS['dark'])

    # Forward arrows
    positions = [1.5, 3.5, 5.5, 7.5, 9.1]
    for i in range(len(positions)):
        ax.annotate('', xy=(positions[i]+0.1, 1.4), xytext=(positions[i]-0.1, 1.4),
                    arrowprops=dict(arrowstyle='->', color=COLORS['dark'], lw=1))

    ax.annotate('Gradient flow (backward)', xy=(2.4, 0.6), xytext=(2.4, 1.0),
                arrowprops=dict(arrowstyle='->', color=COLORS['green'], lw=1),
                fontsize=7, color=COLORS['green'], ha='center')

    ax.set_title('Training Flow: Autograd + Mamba Integration', fontsize=13, fontweight='bold', pad=10)
    path = os.path.join(OUTPUT, 'diagrams', 'autograd_mamba_flow.png')
    save(path)

def plot_benchmark_timeline():
    fig, ax = plt.subplots(figsize=(8, 2.5))
    ax.set_xlim(0, 10); ax.set_ylim(0, 2)
    ax.axis('off')

    events = [
        (0.5, 'task-87\n~2000 tok/s', COLORS['grey']),
        (2.5, 'Phase 20\n(pre-fix)\n~7676 tok/s', COLORS['red']),
        (5.0, 'Memory leak\ndiscovered', COLORS['orange']),
        (6.5, 'Safety fuse\nimplemented', COLORS['orange']),
        (8.0, 'Phase 20\n(post-fix)\n~5659 tok/s', COLORS['green']),
    ]

    for x, label, color in events:
        ax.plot(x, 1.2, 'o', color=color, markersize=12)
        ax.text(x, 1.2, '  ' if len(label.split('\n')) <= 2 else '', fontsize=12, color='white', ha='center', va='center')
        ax.text(x, 0.3, label, ha='center', va='top', fontsize=7.5, color=COLORS['dark'])
        if x > 0.5:
            ax.plot([prev_x, x], [1.2, 1.2], '-', color=COLORS['grey'], lw=1.5)
        prev_x = x

    ax.set_title('Benchmark Timeline: Instability to Stability', fontsize=13, fontweight='bold', pad=10)
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
