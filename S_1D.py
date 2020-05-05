import numpy as np


class S:
    def __init__(self, s1):
        self.I1 = (s1 ** 2)
        self.I2 = 1 / 2 * (self.I1 ** 2 - (s1 ** 4))
        self.I3 = (s1 ** 2)
        self.C = s1**2
        self.invC = 1/self.C

    def Snh(self, mu, lamb):
        mu=np.abs(mu)
        lamb=np.abs(lamb)
        snh = mu * (1 - self.invC) + lamb / 2.0 * (self.I3 - 1) * self.invC
        return snh
    '''
    def Smld(self, alf1m, k1, alf2m, k2):
        # we assume that the strain on the fiber is identical to the strain on the bulk
        if self.I2 - 3<0:
            self.I2=4
        smld = 2.0 * alf1m * k1 * ((self.I1) ** (alf1m - 1.0)) + 2.0 * alf2m * k2 * (
                    (self.I2 - 3) ** (alf2m - 1)) * (self.I1 - self.C)
        return smld
    '''

    def Sf(self, alf1f, k1f, mf):
        if self.I1 - 1 > 0:
            k1f = k1f
        else:
            k1f = 0
        if alf1f<1:
            alf1f=alf1f+1
        else:
            alf1f=alf1f
        sf = 2 * alf1f * k1f * ((self.I1 - 1) ** (alf1f - 1)) * mf
        return sf


    def S(self, mu, lamb, vf, alf1f, k1f, mf): #alf1m, k1, alf2m, k2,
        # There's an unknown number of fibers. This is going to treat the fibers as 1 fiber with bulk properties and direction aligned with the bulk material.
        vm=1-vf
        s = vm * (self.Snh(mu, lamb)) + vf * self.Sf(alf1f, k1f, mf) #+ self.Smld(alf1m, k1, alf2m, k2))
        return s
