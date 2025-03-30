from transformers import pipeline
import gradio as gr

pipe = pipeline(model="RodrigoFardin/whisper-small-pt-br") 
def transcribe(audio):
    text = pipe(audio)["text"]
    return text

iface = gr.Interface(
    fn=transcribe,
    inputs=gr.Audio(type="filepath"),
    outputs="text",
    title="Whisper Small Portuguese",
    description="Realtime demo for Portugues-Brazil speech recognition using a fine-tuned Whisper small model.",
)

iface.launch()
