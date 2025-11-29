import { useState } from 'react'
import axios from 'axios'
import './App.css'

function App() {
  // Pega o ano atual do sistema automaticamente
  const anoAtual = new Date().getFullYear()

  const [formData, setFormData] = useState({
    ano: anoAtual, // Começa preenchido com 2025 (ou o ano que estiver)
    km: '',
    motor: '1.0',
    marca: '1'
  })
  
  const [resultado, setResultado] = useState(null)
  const [loading, setLoading] = useState(false)

  // SEU LINK DA AZURE
  const API_URL = "https://ml-flask-g8cje0b8d5bjhwg6.eastus2-01.azurewebsites.net/api/predict"

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    })
  }

  // Função para formatar dinheiro (O jeito profissional)
  const formatarDinheiro = (valor) => {
    return new Intl.NumberFormat('pt-BR', {
      style: 'currency',
      currency: 'BRL'
    }).format(valor)
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    
    // Validação Básica no Frontend (Tratamento de Erro)
    if (formData.ano < 1900 || formData.ano > anoAtual + 1) {
      alert("Por favor, insira um ano válido.")
      return
    }
    if (formData.km < 0) {
      alert("A quilometragem não pode ser negativa.")
      return
    }

    setLoading(true)
    setResultado(null)

    try {
      const response = await axios.post(API_URL, {
        ano: Number(formData.ano),
        km: Number(formData.km),
        motor: Number(formData.motor),
        marca: Number(formData.marca)
      })
      
      // Agora pegamos o número puro e guardamos no estado
      setResultado(response.data.valor_estimado)
      
    } catch (error) {
      console.error("Erro:", error)
      alert("Erro ao conectar. Tente novamente.")
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="container">
      <div className="card">
        <h1>🚗 Avaliador de Carros</h1>
        <p>Inteligência Artificial para Precificação</p>
        
        <form onSubmit={handleSubmit}>
          
          <div className="input-group">
            <label>Ano de Fabricação</label>
            <input 
              type="number" 
              name="ano" 
              // Validação HTML nativa
              min="1990" 
              max={anoAtual + 1} 
              value={formData.ano} 
              onChange={handleChange} 
              required 
            />
          </div>

          <div className="input-group">
            <label>Quilometragem (KM)</label>
            <input 
              type="number" 
              name="km" 
              placeholder="Ex: 50000" 
              min="0" // Impede negativos pelo teclado numérico
              value={formData.km} 
              onChange={handleChange} 
              required 
            />
          </div>

          <div className="input-group">
            <label>Potência do Motor</label>
            <select name="motor" value={formData.motor} onChange={handleChange}>
              <option value="1.0">1.0</option>
              <option value="1.4">1.4</option>
              <option value="1.6">1.6</option>
              <option value="2.0">2.0</option>
              <option value="2.5">2.5</option>
            </select>
          </div>

          <div className="input-group">
            <label>Categoria da Marca</label>
            <select name="marca" value={formData.marca} onChange={handleChange}>
              <option value="1">Popular (Fiat, VW, GM...)</option>
              <option value="2">Intermediário (Toyota, Jeep, Honda...)</option>
              <option value="3">Luxo (BMW, Audi, Mercedes...)</option>
            </select>
          </div>
          
          <button type="submit" disabled={loading}>
            {loading ? 'Calculando...' : 'Ver Valor de Mercado'}
          </button>
        </form>

        {resultado && (
          <div className="resultado">
            <h3>Valor de Mercado:</h3>
            {/* Aqui aplicamos a formatação PT-BR no número */}
            <h2 className="valor">{formatarDinheiro(resultado)}</h2>
          </div>
        )}
      </div>
    </div>
  )
}

export default App