from predict import predict_image, predict_imgURL

dataURL = "data:image/png;base64,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"

predict_imgURL(dataURL)
