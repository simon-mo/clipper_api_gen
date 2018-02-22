model = dict(
    name="The name of the deployed model",
    version=
    "The version to assign this model. Versions must be unique on a per-model basis, but may be re-used across different models.",
    input_type=
    'The type of the request data this endpoint can process. Input type can be one of "integers", "floats", "doubles", "bytes", or "strings". See the `User Guide <http://clipper.ai/user_guide/#input-types>`_ for more details on picking the right input type for your application.',
    image=
    "A docker image name. If provided, the image will be recorded as part of the model descrtipin in Clipper when registering the model but this method will make no attempt to launch any containers with this image.",
    labels=
    "A list of strings annotating the model. These are ignored by Clipper and used purely for user annotations.",
    batch_size=
    "The user-defined query batch size for the model. Replicas of the model will attempt to process at most `batch_size` queries simultaneously. They may process smaller batches if `batch_size` queries are not immediately available. If the default value of -1 is used, Clipper will adaptively calculate the batch size for individual replicas of this model."
)

app = dict(
    name="The unique name of the application.",
    input_type=
    'The type of the request data this endpoint can process. Input type can be one of "integers", "floats", "doubles", "bytes", or "strings".',
    default_output=
    'The default output for the application. The default output will be returned whenever an application is unable to receive a response from a model within the specified query latency SLO (service level objective). The reason the default output was returned is always provided as part of the prediction response object.',
    latency_slo_micros=
    'The query latency objective for the application in microseconds. This is the processing latency between Clipper receiving a request and sending a response. It does not account for network latencies before a request is received or after a response is sent. If Clipper cannot process a query within the latency objective, the default output is returned. Therefore, it is recommended that he SLO not be set aggressively low unless absolutely necessary. 100000 (100ms) is a good starting value, but the optimal latency objective will vary depending on the application.'
)

misc = dict(
    boolean=
    "If False, only necessary values like names will be returned; if True, more information will be provided.",
    model_version=
    'str | obj with __str__ representation. The version of the model. Note that `version` must be a model version that has already been deployed.'
)

api = dict(
    title="Clipper API",
    description=
    "REST API for instrumenting with Clipper. \nThe admin address can be obtained from querying ClipperConnection.cm.get_admin_addr()"
)
