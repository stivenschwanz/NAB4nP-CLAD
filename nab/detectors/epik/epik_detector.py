from nab.detectors.base import AnomalyDetector
from wnnlib.algos import NPCLAD


class EpikDetector(AnomalyDetector):

    def __init__(self, *args, **kwargs):
        super(EpikDetector, self).__init__(*args, **kwargs)

        # Model parameters
        cs = 2 ** 10
        ps = 2 ** 3
        alphas = 2 ** -12
        az = 64
        bz = 2 ** 2 + 2
        cz = 2 ** 10
        dz = 2 ** 10
        pz = 2 ** 3
        alphaz = 2 ** -12
        test = 2
        min_overlap = 52  # Minimum overlap between the predicted observation and the encoded observation
        delta = 2 * az - 2 * min_overlap
        tau = 0.75
        learning_rate = 2 ** 2
        sub_seq_len = 2 ** 4

        # Create detector
        self.detector = NPCLAD.NPCLAD(cs=cs, ps=ps, alphas=alphas,
                                      az=az, bz=bz, cz=cz, dz=dz, pz=pz, alphaz=alphaz,
                                      test=test, delta=delta, tau=tau,
                                      learning_rate=learning_rate, sub_seq_len=sub_seq_len)

    def initialize(self):
        # Initialize the detector

        self.detector.initialize(self.inputMin, self.inputMax, self.dataSet.data.shape[0])






        
    def handleRecord(self, inputData):
        value = inputData["value"]



        # Handle the input value
        _, score, _, _, _, _ = self.detector.handle(value)



        return (score,)
