---
layout: page
permalink: /research/
title: research
description: Stochastic optimization and exact decomposition for scheduling under uncertainty.
nav: true
nav_order: 1
---

## Interests

- **Methodology:** two-stage and multi-stage stochastic programming; mixed-integer recourse; integer L-shaped and Benders decomposition; branch-and-cut; multi-objective and set-valued optimization
- **Applications:** healthcare operations and outpatient appointment scheduling; airline and air cargo network planning; semiconductor process control; supply chain analytics

---

## Projects

**Stochastic appointment scheduling with overbooking and walk-ins**
*with T. Giovannelli, K. S. Shehadeh, and J. Shi. In final co-author review, 2026.*

- Two-stage stochastic program over a multi-provider clinic session; first stage assigns patients to providers and slots and designates double-booked and open-access slots
- Recourse is a mixed-integer program with bilinear terms, under five sources of uncertainty: arrival deviations, walk-in arrivals, service durations, no-shows, short-notice cancellations
- Enhanced integer L-shaped algorithm in single-tree branch-and-cut, with scenario-wise integer optimality cuts, no-good feasibility cuts, McCormick envelopes, and symmetry-breaking inequalities
- Every instance of the flexible walk-in model with up to 300 scenarios solved to optimality; symmetry breaking reduces multi-hour instances to a small fraction of the time limit
- Structural finding: once demand exceeds nominal capacity, optimal schedules rely entirely on double-booking and reserve no open-access capacity; flexible cross-provider reassignment is the more effective access mechanism
- Presented at IISE 2026 and MOPTA 2026; INFORMS Annual Meeting, November 2026

**Set-valued formulation of open-access allocation**
*with T. Giovannelli. In preparation, 2026.*

- Single-provider session on a fixed slot grid; binary first stage selects slots held open for same-day demand
- Recourse is a multi-objective linear program in three criteria: waiting time of attending patients, session completion time, and unmet same-day demand
- The nondominated set is treated as a random closed set, minimized in the set-valued sense through the selection expectation defined by the Aumann integral
- Binary first stage distinguishes the problem from the continuous-first-stage results in the literature
- Returns the full set of efficient allocations rather than one schedule per assumed weight vector

**Stochastic evaluation for air cargo network planning**
*Atlas Air, Network Planning, 2026.*

- Scenario-based framework with mixed-integer recourse in Pyomo, HiGHS, and Gurobi
- Monte Carlo evaluation of the recourse value function to quantify network disruption cost across fleet flow, capacity utilization, routing, capacity spill, and cascading delay

**Virtual metrology for chemical mechanical planarization**
*with X. Han and X. Jia. ASME MSEC 2024.*

- Dual linear Kalman filter for material removal rate prediction
- Lowest mean squared error against multiple linear regression, EWMA, and Bayesian ARX baselines

**Multi-task survival modeling of post-heart-transplant outcomes**
*with X. Chen, M. Gentili, and J. Trivedi. INFORMS 2022, Research!Louisville 2022.*

- Multi-task Cox proportional hazards model treating each transplantation center as a task over a shared representation
- National registry records integrated with tract-level deprivation measures within a 200-mile radius of each center
- Benchmarked against CoxPH and non-linear CoxPH by concordance index

---

## Directions

**Clinic networks with shared providers.** Extending the first stage to joint assignment and routing across sites that share providers. Scenario subproblems separate by site only when routing is fixed, so the decomposition structure changes. Goal: characterize when the coupled problem stays tractable, and quantify same-day access gained against additional patient travel.

**Scalability of exact decomposition.** Four routes to instances at full-clinic-day scale: optimality cuts strengthened through the scheduling polytope, cut aggregation across scenario subsets, warm-starting branch-and-cut from heuristic policies including iterated local search, and parallel scenario evaluation. Results apply to two-stage programs with mixed-integer recourse generally.

**Patient-level access as a criterion.** Expected delay is an average, and a schedule can minimize it while placing the same patients late every session. Formulating max-min access, dispersion across patient classes, and chance constraints on per-class delay yields the cost-access trade-off surface rather than one point on it.

---

## Undergraduate projects

Self-contained components suitable for final-year projects, each requiring one programming course and one operations research course:

- Scenario generation and reduction from clinic arrival and attendance records
- Discrete-event simulation models for validating the recourse approximation
- Sensitivity studies across cost profiles
- Benchmarking heuristic policies against exact solutions
- Decision-support interfaces presenting a trade-off surface in operational terms
