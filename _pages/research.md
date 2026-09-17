---
layout: page
permalink: /research/
title: research
description: Exact optimization methods for service systems in which capacity is committed before demand is realized.
nav: true
nav_order: 1
---

## Overview

Amanat Ur Rahman's research develops exact optimization methods for service systems in which capacity is committed before demand and attendance are realized. The methodological core is two-stage stochastic programming with mixed-integer recourse, solved by decomposition within branch-and-cut, together with its extension to problems carrying several conflicting criteria, where the set of recourse solutions rather than a single value is the object of interest.

The principal application is outpatient appointment scheduling, in which slots are assigned weeks in advance and a substantial fraction of patients do not attend as booked. Related work applies stochastic optimization to air cargo network planning and predictive modeling to semiconductor process control.

---

## Current work

### Two-stage stochastic programming for scheduling under no-shows and walk-ins

This work formulates outpatient appointment scheduling with overbooking and walk-ins as a two-stage stochastic program over a multi-provider clinic session. The first stage assigns scheduled patients to providers and slots, designates which slots are double-booked, and reserves slots for walk-in patients under an open-access policy. The second stage determines walk-in admission after five sources of uncertainty are realized: deviations between actual and scheduled arrival times, walk-in arrival times, service durations for both patient streams, no-shows, and short-notice cancellations. The objective minimizes expected operational cost across patient waiting time, provider idle time, provider overtime, and denied walk-in admission.

The recourse problem is itself a mixed-integer program containing bilinear terms that couple continuous service start times with binary sequencing indicators, so decomposition methods developed for a linear second stage do not apply. The algorithm is an enhanced integer L-shaped decomposition implemented as single-tree branch-and-cut, separating linear-programming optimality cuts, scenario-wise integer optimality cuts that enforce the exact recourse value at incumbent first-stage solutions, and no-good feasibility cuts that exclude first-stage patterns with infeasible recourse. The formulation is strengthened by scenario- and patient-specific big-M coefficients, McCormick envelopes that render the second stage mixed-integer linear, and symmetry-breaking inequalities exploiting the exchangeability of identical providers and of scheduled patients within a provider pool.

The symmetry-breaking inequalities prove decisive. Instances that branch-and-cut cannot solve within a multi-hour limit are solved to optimality in a small fraction of that time once these inequalities are added, and the full algorithm solves every instance of the flexible walk-in model with up to 300 sampled scenarios to optimality.

The computational study yields a structural result. Once scheduled demand exceeds nominal slot capacity, the optimal schedule relies entirely on double-booking and reserves no open-access capacity under any tested cost profile or walk-in volume. Reserving a slot guarantees one same-day admission but displaces a scheduled patient into an additional double-booked slot, while the appointments vacated by no-shows and short-notice cancellations already absorb walk-in demand. Flexible reassignment of walk-in patients across providers is the more effective mechanism for improving same-day access, and its value is largest when the clinic is not congested.

Joint work with T. Giovannelli, K. S. Shehadeh, and J. Shi. Presented at the IISE Annual Conference (2026) and MOPTA (2026), with presentation at the INFORMS Annual Meeting scheduled for November 2026.

### Set-valued formulation of open-access allocation

Stochastic appointment scheduling models aggregate conflicting outcomes into a single expected cost by assigning a monetary weight to each. A clinic has no reliable basis for pricing a minute of patient waiting time against a minute of provider time or a minute of unmet same-day demand, and such a formulation returns one schedule per weight vector.

This second line of work retains the outcomes as separate criteria. The setting is a single-provider session on a fixed slot grid, in which the first stage selects which slots are held open for same-day demand. The recourse is a multi-objective linear program in three criteria: total waiting time of attending scheduled patients, session completion time, and unmet same-day demand. Its solutions map to a nondominated set in criterion space. That set is a random closed set, and the first stage minimizes its expected value in the set-valued sense, where the expectation is the selection expectation defined through the Aumann integral. The binary first stage distinguishes this problem from the two-stage stochastic multi-objective programs treated in the literature, which assume a continuous first stage.

The output is the full set of efficient open-access allocations rather than a single schedule conditional on assumed weights. In preparation with T. Giovannelli.

### Related methodological work

Three further projects extend the range of methods in this program. At Atlas Air in 2026, a stochastic evaluation framework with mixed-integer recourse was built for air cargo network planning, quantifying disruption cost through Monte Carlo evaluation of the recourse value function. In semiconductor manufacturing, a dual linear Kalman filter for material removal rate prediction in chemical mechanical planarization attained the lowest mean squared error against multiple linear regression, EWMA, and Bayesian ARX baselines. In health services research, a multi-task Cox proportional hazards model treating each transplantation center as a separate learning task over a shared representation integrated national registry records with tract-level deprivation measures to quantify center-level effects on post-heart-transplant survival.

---

## Research agenda

The goal over the next five years is to bring exact stochastic optimization to the scale at which health systems operate, and to make patient-level access a criterion these models optimize rather than report.

**Direction 1. Clinic networks with shared providers.** Appointment scheduling models treat a clinic in isolation with a fixed provider panel. Health systems operate multiple sites that share providers and can route a patient to whichever site can see them soonest. Extending the first stage to joint assignment and routing changes the decomposition structure, since scenario subproblems separate by site only when routing is fixed. The aim is to characterize when the coupled problem admits a tractable decomposition, and to quantify the same-day access gained by cross-site routing against the additional travel imposed on patients.

**Direction 2. Scalability of exact decomposition.** The integer L-shaped method converges slowly on instances at operational size. Four areas of improvement are planned: optimality cuts strengthened through the structure of the scheduling polytope, cut aggregation across scenario subsets that trades cut count against cut strength, warm-starting the branch-and-cut tree from heuristic policies including iterated local search, and parallel scenario evaluation. Results here apply to two-stage stochastic programs with mixed-integer recourse generally, beyond the scheduling application.

**Direction 3. Patient-level access as an explicit criterion.** Expected patient delay is an average, and a schedule can minimize it while consistently placing a subset of patients late in the queue. Formulating patient-level access criteria directly, through max-min access, dispersion across patient classes, and chance constraints on per-class delay, produces the cost-access trade-off surface rather than a single point on it.

---

## Undergraduate involvement

Several components of this program are self-contained enough for undergraduate projects: scenario generation and reduction from clinic arrival and attendance records, discrete-event simulation models for validating the recourse approximation, sensitivity studies across cost profiles, benchmarking of heuristic policies against exact solutions, and decision-support interfaces that present a trade-off surface in operational terms. Each requires one programming course and one operations research course as preparation, and each produces output the larger project uses.
