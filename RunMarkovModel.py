

import HW10.ParameterClasses as P
import HW10.MarkovModel as MarkovCls
import HW10.SupportMarkovModel as SupportMarkov
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs

print ("q1 part1. the non-stroke associated annual mortality rate is therefore 18*100 - 36.2 per 100,000 population, 17.6 per 1000 person"
       " the rateof stroke-associated death = -ln(1-36.2/100000)=0.00036 "
       "the background (non-stroke associated) mortality events is lamda = - ln(1-17.6/1000) =0.0178 ")

print ("q1 part2. The annual rateof stroke events for our population = -ln (1-15/1000) = 0.015")

print ("q1 part3. the annualrate of transition from state Well to Stroke = 0.015*0.9 =0.0135"
       "the annualrateof transition from state Well to Stroke Death=0.015")

print ('q1 part4.  the annual rate of recurrent stroke events = 0.0135*0.17=0.0023')

print (' q1 part5.  the annual transition rates from state Post-Stroke to Stroke = 0.0135*0.8 = 0.0108'
       'the annual transition rates from state post-stroke  to stroke death =0.0135*0.2=0.0027')

print ('q1 part6 the annualrate of transition from Stroke to Post-Stroke=1/52 =0.019')
# create and cohort
cohort = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.ANTICOAG)

simOutputs = cohort.simulate()

# graph survival curve
PathCls.graph_sample_path(
    sample_path=simOutputs.get_survival_curve(),
    title='Survival curve',
    x_label='Simulation time step',
    y_label='Number of alive patients'
    )

# graph histogram of survival times
Figs.graph_histogram(
    data=simOutputs.get_survival_times(),
    title='Survival times of patients with Stroke',
    x_label='Survival time (years)',
    y_label='Counts',
    bin_width=1
)


# graph histogram of number of strokes
Figs.graph_histogram(
    data=simOutputs.get_if_developed_stroke(),
    title='Number of Strokes per Patient',
    x_label='Strokes',
    y_label='Counts',
    bin_width=1
)

# print outcomes (means and CIs)
SupportMarkov.print_outcomes(simOutputs, 'No treatment:')
