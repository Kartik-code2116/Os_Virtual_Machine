"""
constants.py
────────────
All shared data constants used across pages:
  - PRESETS       : Named process workload scenarios
  - PID_COLORS    : Per-PID colour palette for charts
  - RESULT_KEYS   : Session-state keys written by the C++ engine bridge
  - ALGO_INFO     : Metadata about each scheduling algorithm
"""

# ── Workload presets ──────────────────────────────────────────────────────────
PRESETS: dict[str, list[dict]] = {
    "Standard Mix": [
        {"PID": 1, "Arrival": 0, "Burst": 5, "Priority": 2, "Memory": 100},
        {"PID": 2, "Arrival": 1, "Burst": 3, "Priority": 1, "Memory": 150},
        {"PID": 3, "Arrival": 2, "Burst": 4, "Priority": 3, "Memory": 200},
        {"PID": 4, "Arrival": 4, "Burst": 2, "Priority": 2, "Memory": 100},
    ],
    "Convoy Effect": [
        {"PID": 1, "Arrival": 0, "Burst": 12, "Priority": 2, "Memory": 80},
        {"PID": 2, "Arrival": 1, "Burst": 2,  "Priority": 1, "Memory": 50},
        {"PID": 3, "Arrival": 2, "Burst": 1,  "Priority": 1, "Memory": 60},
        {"PID": 4, "Arrival": 3, "Burst": 2,  "Priority": 3, "Memory": 40},
    ],
    "Memory Stress": [
        {"PID": 1, "Arrival": 0, "Burst": 6, "Priority": 2, "Memory": 180},
        {"PID": 2, "Arrival": 1, "Burst": 4, "Priority": 1, "Memory": 140},
        {"PID": 3, "Arrival": 2, "Burst": 5, "Priority": 3, "Memory": 100},
        {"PID": 4, "Arrival": 3, "Burst": 3, "Priority": 2, "Memory":  90},
    ],
    "Priority Chaos": [
        {"PID": 1, "Arrival": 0, "Burst": 4, "Priority": 4, "Memory": 70},
        {"PID": 2, "Arrival": 1, "Burst": 5, "Priority": 1, "Memory": 90},
        {"PID": 3, "Arrival": 2, "Burst": 3, "Priority": 2, "Memory": 80},
        {"PID": 4, "Arrival": 3, "Burst": 2, "Priority": 3, "Memory": 60},
    ],
    "RR Thrash": [
        {"PID": 1, "Arrival": 0, "Burst": 8, "Priority": 2, "Memory": 60},
        {"PID": 2, "Arrival": 0, "Burst": 7, "Priority": 2, "Memory": 80},
        {"PID": 3, "Arrival": 1, "Burst": 6, "Priority": 1, "Memory": 70},
        {"PID": 4, "Arrival": 2, "Burst": 5, "Priority": 3, "Memory": 90},
    ],
    "Idle CPU Test": [
        {"PID": 1, "Arrival": 0,  "Burst": 3, "Priority": 1, "Memory": 50},
        {"PID": 2, "Arrival": 10, "Burst": 4, "Priority": 2, "Memory": 60},
        {"PID": 3, "Arrival": 20, "Burst": 2, "Priority": 1, "Memory": 40},
    ],
}

# ── PID → Plotly colour palette ───────────────────────────────────────────────
PID_COLORS: dict[int, str] = {
    1: "#63b3ed",
    2: "#48bb78",
    3: "#ed8936",
    4: "#9f7aea",
    5: "#fc8181",
    6: "#38b2ac",
    7: "#f6e05e",
    8: "#b794f4",
    9: "#f687b3",
   10: "#4fd1c5",
}

# ── Session-state result keys written after each simulation run ───────────────
RESULT_KEYS: list[str] = [
    "results",
    "timeline",
    "memory_events",
    "state_events",
    "cpu_events",
    "summary",
    "summary_text",
    "output_dir",
    "algorithm",
    "total_memory",
    "quantum",
    "benchmark_results",
]

# ── Algorithm metadata ────────────────────────────────────────────────────────
ALGO_INFO: dict[str, dict] = {
    "FCFS": {
        "full": "First Come, First Served",
        "type": "Non-Preemptive",
        "type_color": "#63b3ed",
        "description": (
            "Executes processes strictly in arrival order. The simplest possible scheduler. "
            "Has zero overhead but causes the Convoy Effect — short processes wait behind long ones."
        ),
        "pros":  ["Zero overhead", "Fair in arrival order", "No starvation"],
        "cons":  ["Convoy effect", "High average waiting time", "Poor for interactive workloads"],
        "use":   "Batch processing systems",
    },
    "SJF": {
        "full": "Shortest Job First",
        "type": "Non-Preemptive",
        "type_color": "#48bb78",
        "description": (
            "Always picks the process with the smallest burst time from the ready queue. "
            "Provably minimises average waiting time for a given set of processes — but requires "
            "burst time prediction and can starve long jobs."
        ),
        "pros":  ["Minimum avg waiting time", "Good throughput", "Efficient for short tasks"],
        "cons":  ["Requires burst prediction", "Long jobs may starve", "Not preemptive by default"],
        "use":   "Interactive / batch systems with known burst times",
    },
    "Priority": {
        "full": "Priority Scheduling",
        "type": "Non-Preemptive",
        "type_color": "#9f7aea",
        "description": (
            "Dispatches the ready process with the highest priority (lowest numeric value). "
            "Real-time and system processes get priority over user processes. "
            "Without aging, low-priority processes can starve indefinitely."
        ),
        "pros":  ["Prioritises critical tasks", "Flexible", "Models real OS kernels"],
        "cons":  ["Starvation of low-priority", "No aging in this model", "Convoy if priorities tie"],
        "use":   "Real-time systems, OS kernel task queues",
    },
    "Round Robin": {
        "full": "Round Robin",
        "type": "Preemptive",
        "type_color": "#ed8936",
        "description": (
            "Rotates through the ready queue giving each process exactly τ (time quantum) CPU ticks. "
            "The foundation of modern fair-share schedulers. Responsiveness increases with smaller τ, "
            "but context-switch overhead increases proportionally."
        ),
        "pros":  ["Fair CPU sharing", "No starvation", "Good response time"],
        "cons":  ["High context switches", "Quantum choice is tricky", "High overhead for large queues"],
        "use":   "Time-sharing, interactive systems, modern OS kernels",
    },
}
