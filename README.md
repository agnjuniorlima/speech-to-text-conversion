# Speech-to-Text Conversion

Este repositório apresenta um modelo de reconhecimento automático de fala (ASR) em Português do Brasil, baseado no modelo Whisper Small da OpenAI. O fine-tuning foi realizado utilizando a biblioteca `transformers` da Hugging Face.

## 📄 Relatório

Para detalhes sobre o processo de fine-tuning, acesse o relatório completo:
[📥 Download do Relatório](https://github.com/agnjuniorlima/speech-to-text-conversion/blob/main/Fine_Tuning_do_Modelo__whisper_small__para_Reconhecimento_de_Fala_em_Portugu%C3%AAs_BR.pdf)

## 🚀 Como Usar

1. **Baixar o Notebook**
   - Faça o download do notebook de treinamento:
   [📥 fine-tune-whisper-for-pt-asr-with-transformers-v4.ipynb](https://github.com/agnjuniorlima/speech-to-text-conversion/blob/main/fine-tune-whisper-for-pt-asr-with-transformers-v4.ipynb)

2. **Instalar as dependências**
   - Instale as dependências necessárias executando:
     ```bash
     pip install -r requirements.txt
     ```
   - Se estiver rodando em um ambiente do Google Colab, instale manualmente as bibliotecas conforme especificado no notebook.

3. **Carregar o modelo treinado**
   - O modelo fine-tunado pode ser acessado no Hugging Face:  
   [🌍 Whisper Small PT-BR no Hugging Face](https://huggingface.co/RodrigoFardin/whisper-small-pt-br)
   
4. **Download do modelo treinado**
   - Para utilizar o modelo localmente, baixe os pesos treinados:  
   [📥 Download do modelo treinado](https://drive.google.com/file/d/13ACPHxbHNp4P2cWNV13UMULSmk0S9H91/view?usp=sharing)

## 🛠 Tecnologias Utilizadas

- **Linguagem:** Python 3.12.2
- **Bibliotecas:**
  - `datasets==3.4.1`
  - `evaluate==0.4.3`
  - `gradio==5.23.1`
  - `huggingface_hub==0.29.3`
  - `torch==2.6.0`
  - `transformers==4.50.0`
- **Ferramentas:**
  - Hugging Face
  - Deep Learning

## 📬 Contato

Se tiver dúvidas ou sugestões, sinta-se à vontade para entrar em contato!

📧 Rodrigo C. Fardin - [rodrigo.correa.fardin@gmail.com](mailto:rodrigo.correa.fardin@gmail.com)  
📧 Agnelo P. L. Júnior - [agnjuniorlima@gmail.com](mailto:agnjuniorlima@gmail.com)

