from brian import *

# Parameters
C = 281 * pF
gL = 30 * nS
taum = C / gL
EL = -70.6 * mV
VT = -50.4 * mV
DeltaT = 2 * mV
Vcut = VT + 5 * DeltaT

# Pick an electrophysiological behaviour
tauw, a, b, Vr = 144*ms, 4*nS, 0.0805*nA, -70.6*mV # Regular spiking (as in the paper)
# #tauw,a,b,Vr=20*ms,4*nS,0.5*nA,VT+5*mV # Bursting
# #tauw,a,b,Vr=144*ms,2*C/(144*ms),0*nA,-70.6*mV # Fast spiking
#
eqs = """
dvm/dt = (gL*(EL - vm) + gL*DeltaT*exp((vm - VT)/DeltaT) + I - w)/C : volt
dw/dt = (a*(vm - EL) - w)/tauw : amp
I : amp
"""
#
neuron = NeuronGroup(1, model=eqs, threshold='vm>Vcut',
                     reset="vm=Vr; w+=b")
neuron.vm = EL
trace = StateMonitor(neuron, 'vm', record=0)
spikes = SpikeMonitor(neuron)

#####impulse train####

# for i in range(0,20):
#     run(10*ms)
#     neuron.I=2.5*nA;
#     run(defaultclock.dt)
#     neuron.I=0*ms
#######pulse input
run(20 * ms)
neuron.I = 0.5*nA
run(180 * ms)
neuron.I = 0*nA
run(300 * ms)
neuron.I=0.8*nA
run(500*ms)

(i,t)=spikes.it
print 'spike times for impulse train input:'
print t
vm = trace[0]

# We draw nicer spikes
# for tt in t:
#     i = int(tt / defaultclock.dt)
#     vm[i] = 20*mV

plot(trace.times / ms, vm / mV)
xlabel('time (ms)')
ylabel('membrane potential (mV)')
show()



