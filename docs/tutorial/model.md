# Model

## Tensorflow `2.14` Keras `2`
Download drutai **12** predictive models for tensorflow `2.14x` Keras `2x`.

::::{tab-set}
:::{tab-item} Command
:sync: tab1
```{code} python
import drutai

drutai.predict.download_data(
    url='https://github.com/2003100127/drutai/releases/download/model/model.zip',
    sv_fpn='../../data/drutai/model.zip',
)
```
:::
:::{tab-item} Output log
:sync: tab2
```shell
 ____             _        _ 
|  _ \ _ __ _   _| |_ __ _(_)
| | | | '__| | | | __/ _` | |
| |_| | |  | |_| | || (_| | |
|____/|_|   \__,_|\__\__,_|_|
                             

02/04/2025 01:56:13 logger: downloading data...
02/04/2025 01:56:37 logger: downloaded!
```
:::
::::

## Tensorflow `2.19` Keras `3`

In Keras `3`, the approach to loading and calling models has changed significantly compared to Keras `2`, especially when used within the TensorFlow ecosystem. Many legacy TensorFlow models that relied on `tf.keras.Model` subclassing or `SavedModel` formats may now require structural modifications, explicit serialization logic, or migration to the new `.keras` format to ensure compatibility. However, when we attempted to make this transition, the process did not go as smoothly as expected. Please check the [_installation_](../installation.md) guide.

:::{tip} Error reports
:class: dropdown
ValueError: File format not supported: `filepath=self.model_fp`. Keras 3 only supports V3 `.keras` files and legacy H5 format files (`.h5` extension). Note that the legacy SavedModel format is not supported by `load_model()` in Keras 3. In order to reload a TensorFlow SavedModel as an inference-only layer in Keras 3, use `keras.layers.TFSMLayer(self.model_fp, call_endpoint='serving_default')` (note that your `call_endpoint` might have a different name).
:::

Errors continue to reared its head or different ones popped out even though we corrected errors.

:::{tip} Error reports
:class: dropdown
ValueError: Layer count mismatch when loading weights from file. Model expected 0 layers, found 5 saved layers.
:::

We generated a LSTMCNN model for use in Keras 3. You can access it as shown below. Due to a complicated process of conversion, we did not apply it to all models. 

::::{tab-set}
:::{tab-item} Command
:sync: tab1
```{code} python
import drutai

drutai.predict.download_data(
    url='https://github.com/2003100127/drutai/releases/download/model-k3/lstmcnn_k3x.h5',
    sv_fpn='../../data/lstmcnn_k3x.h5',
)
```
:::
:::{tab-item} Output log
:sync: tab2
```{code} shell
 ____             _        _ 
|  _ \ _ __ _   _| |_ __ _(_)
| | | | '__| | | | __/ _` | |
| |_| | |  | |_| | || (_| | |
|____/|_|   \__,_|\__\__,_|_|
                             

02/04/2025 02:00:49 logger: downloading data...
02/04/2025 02:00:50 logger: downloaded!
```
:::
::::
