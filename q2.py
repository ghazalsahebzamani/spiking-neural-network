
from brian import *
from brian.library.ionic_currents import * #in this lib,HH model equations has been predefined.
area= 20000 * umetre **2
Cm=1*ufarad*cm**-2*area
gl=5e-5*siemens*cm**(-2)*area
g_na=100*msiemens*cm**(-2)*area
g_kd=30* msiemens*cm**(-2)*area
VT= -63*mV
duration= 2*second
El = -65 * mV
EK = -90 * mV
ENa = 50 * mV
eqs = MembraneEquation(Cm) + leak_current(gl, El)
eqs += K_current_HH(36 * msiemens, EK) + Na_current_HH(120 * msiemens, ENa)
eqs += Current('I:amp')

G = NeuronGroup(100, eqs,threshold=VT, implicit=True, freeze=True)

#M = SpikeMonitor(G)

G.I = linspace(0 * nA, 1 * nA, 100) #input
counter=SpikeCounter(G)
run(duration)
subplot(211)
plot(G.I / nA, counter.count / duration)
xlabel('I (nA)')
ylabel('Firing rate (Hz)')
show()
