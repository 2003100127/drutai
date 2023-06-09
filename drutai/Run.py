__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import numpy as np
import pandas as pd
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
from drutai.Pipe import fetch


def drestruct(data, met):
    if met == 'ConvMixer64':
        return np.reshape(data, [-1, 108, 108, 1])
    else:
        return data


class predict(object):

    def __init__(
            self,
            smile_fpn,
            fasta_fpn,
            method,
            model_fp,
            sv_fpn,
    ):
        self.method = method
        self.model_fp = model_fp
        self.sv_fpn = sv_fpn
        self.ind = fetch(
            smile_fpn=smile_fpn,
            fasta_fpn=fasta_fpn,
        )

    def m2(self, ):
        loaded_model = tf.keras.models.load_model(self.model_fp)
        pret = loaded_model.predict(drestruct(self.ind, self.method), batch_size=1)
        t = []
        if pret[0][1] > pret[0][0]:
            t.append([pret[0][1], 'Interaction'])
        else:
            t.append([pret[0][0], 'Non-interaction'])
        df = pd.DataFrame(t, columns=['prob', 'predicted_type'])
        df.to_csv(
            self.sv_fpn,
            sep='\t',
            header=True,
            index=False,
        )
        return df

    def m1(self, ):
        sess = tf.Session()
        saver = tf.train.import_meta_graph(self.model_fp + '.meta')
        saver.restore(sess, self.model_fp)
        tf_graph = tf.get_default_graph()
        if self.method != 'ResNet50':
            Placeholder = tf_graph.get_tensor_by_name("Placeholder:0")
            x = tf_graph.get_tensor_by_name("x:0")
            prediction = tf_graph.get_tensor_by_name("pred_softmax:0")
        else:
            x = tf_graph.get_tensor_by_name("x_1:0")
            Placeholder = 1
            prediction = tf_graph.get_tensor_by_name("presoftmax:0")

        pret = self.m1w(
            sess=sess,
            x=x,
            Placeholder=Placeholder,
            prediction=prediction,
            x_test=self.ind,
        )
        t = []
        if pret[0][1] > pret[0][0]:
            t.append([pret[0][1], 'Interaction'])
        else:
            t.append([pret[0][0], 'Non-interaction'])
        df = pd.DataFrame(t, columns=['prob', 'predicted_type'])
        df.to_csv(
            self.sv_fpn,
            sep='\t',
            header=True,
            index=False,
        )
        return df

    def m1w(self, sess, x, prediction, x_test, Placeholder):
        pds = []
        if self.method != 'ResNet50':
            indict = {x: x_test, Placeholder: 1}
        else:
            indict = {x: x_test}
        p_tmp = sess.run(prediction, feed_dict=indict)
        pds.append(p_tmp)
        return pds[0]


if __name__ == "__main__":
    p = predict(
        smile_fpn='data/example/148124.txt',
        fasta_fpn='data/example/A0A0H2UXE9.fasta',

        # method='AlexNet',
        # method='BiRNN',
        # method='RNN',
        method='Seq2Seq',
        # method='ResNet50',
        # method='CNN',
        # method='ConvMixer64',
        # method='DSConv',
        # method='LSTMCNN',
        # method='MobileNet',
        # method='ResNet18',
        # method='SCAResNet',

        # model_fp='model/alexnet/alexnet',
        # model_fp='model/birnn/birnn',
        # model_fp='model/rnn/rnn',
        model_fp='model/seq2seq/seq2seq',
        # model_fp='model/resnet50/resnet50',
        # model_fp='model/cnn',
        # model_fp='model/convmixer64',
        # model_fp='model/dsconv',
        # model_fp='model/lstmcnn',
        # model_fp='model/mobilenetv2',
        # model_fp='model/resnet_prea18',
        # model_fp='model/scaresnet',

        sv_fpn='./pred.drutai',
    )
    print(p.m1())
    # print(p.m2())

