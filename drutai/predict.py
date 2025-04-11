__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2025"
__license__ = "MIT"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import urllib.request
import click
from pyfiglet import Figlet
from drutai.util.Model import Model
from drutai.util.Feature import fetch
from drutai.util.Console import Console


vignette1 = Figlet(font='standard')

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.command(short_help=vignette1.renderText('Drutai'), context_settings=CONTEXT_SETTINGS)
@click.option('-u', '--url', default='https://github.com/2003100127/drutai/releases/download/model/model.zip', help='URL of drutai models')
@click.option('-o', '--sv_fpn', default='./model.zip', help='output path of drutai models')
def download(url, sv_fpn):
    download_data(url, sv_fpn)


def download_data(
        url,
        sv_fpn,
        verbose=True,
):
    console = Console()
    console.verbose = verbose
    print(vignette1.renderText('Drutai'))
    console.print('downloading data...')
    urllib.request.urlretrieve(
        url=url,
        filename=sv_fpn,
    )
    console.print('downloaded!')
    return


class HelpfulCmd(click.Command):
    def format_help(self, ctx, formatter):
        click.echo(vignette1.renderText('Drutai'))
        click.echo(
            '''
            -m, --method, 
                A deep learning method. It can be any below.
                AlexNet | BiRNN | RNN | Seq2Seq | 
                CNN | ConvMixer64 | DSConv | LSTMCNN |
                MobileNet | ResNet18 | ResNet50 | SEResNet |
            '''
        )
        click.echo(
            '''
            -br, --br_fpn, binary relations between small molecules and protein targets
            '''
        )
        click.echo(
            '''
            -d, --smile_fpn, map between small molecule IDs and their smile strings
            '''
        )
        click.echo(
            '''
            -t, --fasta_fp, protein target fasta file paths
            '''
        )
        click.echo(
            '''
            -mf, --model_fp, a model path
            '''
        )
        click.echo(
            '''
            -o, --sv_fpn, outputting drutai predictions
            '''
        )


@click.command(cls=HelpfulCmd, context_settings=CONTEXT_SETTINGS)
@click.option(
    '-m', '--method', default='LSTMCNN',
    help='''
        A deep learning method. It can be any below.
        AlexNet | BiRNN | RNN | Seq2Seq | 
        CNN | ConvMixer64 | DSConv | LSTMCNN |
        MobileNet | ResNet18 | ResNet50 | SEResNet |
    '''
)
@click.option('-br', '--br_fpn', default='./data/input/br_sm_target.txt', help='binary relations between small molecules and protein targets')
@click.option('-d', '--smile_fpn', default='./data/input/br_smile.txt', help='map between small molecules and their smile strings')
@click.option('-t', '--fasta_fp', default='./data/example/', help='protein target fasta file paths')
@click.option('-mf', '--model_fp', default='./data/model/lstmcnn', help='a model path')
@click.option('-o', '--sv_fpn', default='./data/out.drutai', help='outputting drutai predictions')
@click.option('-vb', '--verbose', default=True, help='console output')
def run(
        br_fpn,
        smile_fpn,
        fasta_fp,
        method,
        model_fp,
        sv_fpn,
        verbose,
):
    sm_target_interaction(
        br_fpn=br_fpn,
        smile_fpn=smile_fpn,
        fasta_fp=fasta_fp,
        method=method,
        model_fp=model_fp,
        sv_fpn=sv_fpn,
        verbose=verbose,
    )



def sm_target_interaction(
        br_fpn,
        smile_fpn,
        fasta_fp,
        method,
        model_fp,
        sv_fpn,
        verbose=True,
):
    console = Console()
    console.verbose = verbose
    print(vignette1.renderText('Drutai'))
    console.print('=>Prediction starts...')
    mat_np = fetch(
        br_fpn,
        smile_fpn,
        fasta_fp,
    )
    drutai_p = Model(
        mat_np=mat_np,
        method=method,
        model_fp=model_fp,
        sv_fpn=sv_fpn,
    )
    s = [
        'AlexNet',
        'BiRNN',
        'RNN',
        'Seq2Seq',
    ]
    if method in s:
        drutai_p.m1()
    else:
        drutai_p.m2()


if __name__ == '__main__':
    external = False # True False

    if external:
        run()
    else:
        params = {
            'br_fpn': '../data/input/br_sm_target.txt',
            'smile_fpn': '../data/input/br_smile.txt',
            'fasta_fp': '../data/input/',
            'method': 'AlexNet',
            # 'method': 'BiRNN',
            # 'method': 'RNN',
            # 'method': 'Seq2Seq',
            # 'method': 'CNN',
            # 'method': 'ConvMixer64',
            # 'method': 'DSConv',
            # 'method': 'LSTMCNN',
            # 'method': 'MobileNet',
            # 'method': 'ResNet18',
            # 'method': 'ResNet50',
            # 'method': 'SEResNet',

            'model_fp': '../data/model/alexnet/alexnet',
            # 'model_fp': '../data/model/birnn/birnn',
            # 'model_fp': '../data/model/cnn',
            # 'model_fp': '../data/model/convmixer64',
            # 'model_fp': '../data/model/dsconv',
            # 'model_fp': '../data/model/lstmcnn',
            # 'model_fp': '../data/model/mobilenet',
            # 'model_fp': '../data/model/resnet_prea18',
            # 'model_fp': '../data/model/resnet_prea50',
            # 'model_fp': '../data/model/rnn/rnn',
            # 'model_fp': '../data/model/seq2seq/seq2seq',
            # 'model_fp': '../data/model/seresnet',

            'sv_fpn': '../data/output/pred.drutai',
        }
        # sm_target_interaction(
        #     br_fpn=params['br_fpn'],
        #     smile_fpn=params['smile_fpn'],
        #     fasta_fp=params['fasta_fp'],
        #     method=params['method'],
        #     model_fp=params['model_fp'],
        #     sv_fpn=params['sv_fpn'],
        # )

        # download data
        download_data(
            url='https://github.com/2003100127/deepdlncud/releases/download/model/model.zip',
            sv_fpn='../data/model.zip',
        )