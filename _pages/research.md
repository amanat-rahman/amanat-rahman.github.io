---
layout: page
permalink: /research/
title: research
description: Stochastic optimization and exact decomposition for scheduling under uncertainty.
nav: true
nav_order: 1
---

## Research interests

- **Methodology**
  - Two-stage and multi-stage stochastic programming
  - Mixed-integer recourse; integer L-shaped and Benders decomposition
  - Branch-and-cut and cut generation
  - Multi-objective and set-valued optimization
- **Applications**
  - Healthcare operations and outpatient appointment scheduling
  - Airline and air cargo network planning
  - Semiconductor manufacturing process control
  - Supply chain analytics

---

## Projects

- **Stochastic appointment scheduling with overbooking and walk-ins**
  - *With T. Giovannelli, K. S. Shehadeh, and J. Shi. In final co-author review, 2026.*
  - **Model.** Two-stage stochastic program over a multi-provider clinic session. The first stage assigns patients to providers and slots and designates double-booked and open-access slots.
  - **Uncertainty.** Five sources: arrival-time deviations, walk-in arrivals, service durations, no-shows, and short-notice cancellations.
  - **Difficulty.** The recourse problem is itself a mixed-integer program with bilinear terms, so decomposition methods built for a linear second stage do not apply.
  - **Algorithm.** Enhanced integer L-shaped method in single-tree branch-and-cut, with scenario-wise integer optimality cuts, no-good feasibility cuts, McCormick envelopes, and symmetry-breaking inequalities.
  - **Computation.** Every instance of the flexible walk-in model with up to 300 scenarios solved to optimality. Symmetry breaking reduces instances unsolved at a multi-hour limit to a small fraction of that time.
  - **Finding.** Once demand exceeds nominal capacity, optimal schedules rely entirely on double-booking and reserve no open-access capacity. Flexible cross-provider reassignment is the more effective access mechanism.
  - **Presented.** IISE 2026, MOPTA 2026; INFORMS Annual Meeting, November 2026.

- **Set-valued formulation of open-access allocation**
  - *With T. Giovannelli. In preparation, 2026.*
  - **Setting.** Single-provider session on a fixed slot grid; a binary first stage selects which slots are held open for same-day demand.
  - **Recourse.** Multi-objective linear program in three criteria: waiting time of attending patients, session completion time, and unmet same-day demand.
  - **Approach.** The nondominated set is treated as a random closed set and minimized in the set-valued sense, through the selection expectation defined by the Aumann integral.
  - **Contribution.** The binary first stage separates this problem from the continuous-first-stage results in the literature.
  - **Output.** The full set of efficient allocations, rather than one schedule per assumed weight vector.

- **Stochastic evaluation for air cargo network planning**
  - *Atlas Air, Network Planning, 2026.*
  - **Framework.** Scenario-based evaluation with mixed-integer recourse in Pyomo, HiGHS, and Gurobi.
  - **Use.** Monte Carlo evaluation of the recourse value function quantifies disruption cost across fleet flow, capacity utilization, routing, capacity spill, and cascading delay.

- **Virtual metrology for chemical mechanical planarization**
  - *With X. Han and X. Jia. ASME MSEC 2024.*
  - **Method.** Dual linear Kalman filter for material removal rate prediction.
  - **Result.** Lowest mean squared error against multiple linear regression, EWMA, and Bayesian ARX baselines.

- **Multi-task survival modeling of post-heart-transplant outcomes**
  - *With X. Chen, M. Gentili, and J. Trivedi. INFORMS 2022; Research!Louisville 2022.*
  - **Method.** Multi-task Cox proportional hazards model treating each transplantation center as a task over a shared representation.
  - **Data.** National registry records integrated with tract-level deprivation measures within a 200-mile radius of each center.
  - **Benchmark.** Evaluated against CoxPH and non-linear CoxPH by concordance index.

---

## Research directions

- **Clinic networks with shared providers**
  - Extend the first stage to joint assignment and routing across sites that share providers
  - Scenario subproblems separate by site only when routing is fixed, so the decomposition structure changes
  - Goal: characterize when the coupled problem stays tractable, and quantify same-day access gained against added patient travel

- **Scalability of exact decomposition**
  - Optimality cuts strengthened through the structure of the scheduling polytope
  - Cut aggregation across scenario subsets, trading cut count against cut strength
  - Warm-starting branch-and-cut from heuristic policies, including iterated local search
  - Parallel scenario evaluation
  - Results apply to two-stage programs with mixed-integer recourse generally

- **Patient-level access as an explicit criterion**
  - Expected delay is an average; a schedule can minimize it while placing the same patients late every session
  - Formulate max-min access, dispersion across patient classes, and chance constraints on per-class delay
  - Goal: compute the cost-access trade-off surface rather than one point on it

---

## Undergraduate research

Self-contained components suitable for final-year projects, each requiring one programming course and one operations research course:

- Scenario generation and reduction from clinic arrival and attendance records
- Discrete-event simulation for validating the recourse approximation
- Sensitivity studies across cost profiles
- Benchmarking heuristic policies against exact solutions
- Decision-support interfaces presenting a trade-off surface in operational terms
