from flask import Flask, request, jsonify
from .models import Material, Parede, Porta, Janela
from .services import calcular_quantidade_montantes, calcular_quantidade_placas, calcular_quantidade_parafusos, Parede

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Calculadora Orelha Seca - API'}), 200

@app.route('/calcular_parede', methods=['POST'])
def calcular_parede():
    try:
        # Recebe os dados da parede no JSON
        dados_parede = request.get_json()

        # Cria um objeto Parede com os dados recebidos
        parede = Parede(
            comprimento=dados_parede['comprimento'],
            altura=dados_parede['altura'],
            tipo=dados_parede['tipo'],
            portas=dados_parede.get('portas', []),
            janelas=dados_parede.get('janelas', [])
        )

        # Calcula os materiais
        area_parede = parede.calcular_area()
        montantes = parede.calcular_montantes()
        placas = parede.calcular_placas(lados_plaqueados=dados_parede['lados_plaqueados'])
        parafusos = calcular_quantidade_parafusos(area_parede, parede.tipo, espacamento_montantes=0.60)

        # Retorna os resultados em um JSON
        return jsonify({
            'area_parede': area_parede,
            'montantes': montantes,
            'placas': placas,
            'parafusos': parafusos
        }), 200

    except ValueError as e:
        return jsonify({'error': str(e)}), 400

    except Exception as e:
        return jsonify({'error': 'Ocorreu um erro ao calcular os materiais.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
