# Fine-tuning do Whisper para Reconhecimento de Fala em Português-BR

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
   
4. **Alternativamente, o modelo treinado esta diponível no Google Drive**
   - O modelo fine-tunado pode ser acessado no Google Drive: 
   [📥 Download do modelo treinado](https://drive.google.com/file/d/1nr8kc4ih4Gr0lloSW5Y00uO1iajou0ae/view?usp=sharing)


## 🧪 Testando o Modelo

Você pode testar o modelo treinado utilizando a interface Gradio inclusa no arquivo `test_model.py`.

### Como rodar o teste:

1. **Baixe o arquivo de teste:**
   - [📥 test_model.py](test_model.py)

2. **Instale as dependências:**
   - Crie um ambiente virtual e instale as dependências:
     ```bash
     pip install -r requirements.txt
     ```

3. **Execute o script de teste:**
   - Execute o arquivo `test_model.py`:
     ```bash
     python test_model.py
     ```

4. **Uso da Interface:**
   - A interface Gradio será aberta no seu navegador. Você pode carregar um arquivo de áudio e o modelo irá transcrever a fala em texto em tempo real.

### 🎥 Demonstração do Modelo

Veja abaixo um vídeo demonstrando o uso do modelo:

[📹 Demonstração do Modelo](https://youtu.be/54hdstBkMGQ) 

## 🛠 Tecnologias Utilizadas

- **Linguagem:** Python 3.12.2
- **Bibliotecas:**
  - `datasets==3.4.1`
  - `evaluate==0.4.3`
  - `gradio==5.23.1`
  - `huggingface_hub==0.29.3`
  - `torch==2.6.0`
  - `transformers==4.50.0`

- **Ferramentas Utilizadas:**
   - **Whisper** – Modelo de reconhecimento de fala desenvolvido pela OpenAI, utilizado para o fine-tuning e transcrição de áudio.
   - **Transformers** – Biblioteca da Hugging Face para trabalhar com modelos de NLP e ASR, utilizada para o fine-tuning do modelo Whisper.
   - **Hugging Face** – Plataforma para hospedagem e compartilhamento de modelos de aprendizado de máquina.
   - **Deep Learning** – Técnicas de aprendizado profundo aplicadas para o treinamento e ajuste do modelo.

## 📬 Contato

Se tiver dúvidas ou sugestões, sinta-se à vontade para entrar em contato!

📧 Rodrigo C. Fardin - [rodrigo.correa.fardin@gmail.com](mailto:rodrigo.correa.fardin@gmail.com)  
📧 Agnelo P. L. Júnior - [agnjuniorlima@gmail.com](mailto:agnjuniorlima@gmail.com)  
📧 Luiz R. A. de Araujo - [luiz.r.araujo@edu.ufes.br](mailto:luiz.r.araujo@edu.ufes.br)


