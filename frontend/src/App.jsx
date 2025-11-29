import { useState } from 'react'
import axios from 'axios'
import './App.css'

function App() {
  // 1. Pega o ano atual do computador (ex: 2025)
  const anoAtual = new Date().getFullYear()

  const [formData, setFormData] = useState({
    ano: anoAtual, // 2. Começa já preenchido
    km: '',
    motor: '1.0', 
    marca: '1'    
  })
  
  const [resultado, setResultado] = useState(null)
  const [loading, setLoading] = useState(false)

  const API_URL = "https://ml-flask-g8cje0b8d5bjhwg6.eastus2-01.azurewebsites.net/api/predict"

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    })
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    setResultado(null)

    try {
      const response = await axios.post(API_URL, {
        ano: Number(formData.ano),
        km: Number(formData.km),
        motor: Number(formData.motor),
        marca: Number(formData.marca)
      })
      
      setResultado(response.data)
    } catch (error) {
      console.error("Erro:", error)
      alert("Erro ao conectar. O servidor Azure pode estar 'dormindo'. Tente de novo em 30 segundos.")
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="container">
      <div className="card">
        <h1>🚗 Avaliador de Carros</h1>
        <p>Previsão de Preço com IA</p>
        
        <form onSubmit={handleSubmit}>
          
          <div className="input-group">
            <label>Ano de Fabricação</label>
            <input 
              type="number" name="ano" placeholder="Ex: 2020" 
              // 3. Validação: Impede anos absurdos
              min="1990"
              max={anoAtual + 1}
              value={formData.ano} onChange={handleChange} required 
            />
          </div>

          <div className="input-group">
            <label>Quilometragem (KM)</label>
            <input 
              type="number" name="km" placeholder="Ex: 50000" 
              // 4. Validação: Impede negativo
              min="0"
              value={formData.km} onChange={handleChange} required 
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
            {loading ? 'Calculando...' : 'Ver Preço Estimado'}
          </button>
        </form>

        {resultado && (
          <div className="resultado">
            <h3>Valor de Mercado:</h3>
            <h2 className="valor">{resultado}</h2>
          </div>
        )}
      </div>
    </div>
  )
}

export default App