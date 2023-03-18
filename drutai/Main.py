__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import urllib.request
import click
from pyfiglet import Figlet
from drutai.Run import predict

vignette1 = Figlet(font='standard')

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.command(short_help=vignette1.renderText('Drutai'), context_settings=CONTEXT_SETTINGS)
@click.option('-u', '--url', default='https://github.com/2003100127/drutai/releases/download/model/model.zip', help='URL of drutai models')
@click.option('-o', '--output_path', default='./model.zip', help='output path of drutai models')
def download(url, output_path):
    print(vignette1.renderText('Drutai'))
    print('downloading...')
    urllib.request.urlretrieve(
        url=url,
        filename=output_path,
    )
    print('downloaded!')
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
            -d, --smile_fpn, a drug file that contains the smile string
            '''
        )
        click.echo(
            '''
            -t, --fasta_fpn, a protein fasta file
            '''
        )
        click.echo(
            '''
            -mf, --model_fp, a model path
            '''
        )
        click.echo(
            '''
            -o, --output_path, outputting drutai predictions
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
@click.option('-d', '--smile_fpn', default='data/example/148124.txt', help='a drug file that contains the smile string')
@click.option('-t', '--fasta_fpn', default='data/example/A0A0H2UXE9.fasta', help='a protein fasta file')
@click.option('-mf', '--model_fp', default='model/lstmcnn', help='a model path')
@click.option('-o', '--output_path', default='./out.drutai', help='outputting drutai predictions')
def main(
        method,
        smile_fpn,
        fasta_fpn,
        model_fp,
        output_path,
):
    print(vignette1.renderText('Drutai'))
    print('predicting...')
    drutai_p = predict(
        smile_fpn=smile_fpn,
        fasta_fpn=fasta_fpn,
        method=method,
        model_fp=model_fp,
        sv_fpn=output_path,
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
    main()