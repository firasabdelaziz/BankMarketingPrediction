from django.shortcuts import render
from .forms import PredictionForm
from .utils import prediction_model


def predict_view(request):
    result = None
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            # Get form data
            contact_duration = form.cleaned_data['contact_duration']
            employment_variation_rate = form.cleaned_data['employment_variation_rate']
            client_age = form.cleaned_data['client_age']

            # Make prediction using the model
            prediction_result = prediction_model.predict(
                contact_duration,
                employment_variation_rate,
                client_age
            )

            if prediction_result['success']:
                result = {
                    'prediction': round(prediction_result['prediction'], 2)
                }
            else:
                result = {'error': prediction_result['error']}
    else:
        form = PredictionForm()

    return render(request, 'prediction/predict.html', {
        'form': form,
        'result': result
    })
