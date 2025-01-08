import { useNavigate } from "react-router-dom"

export function SuccesfulIssue() {
  const navigate = useNavigate()

  return (
    <>
      <h1>Succesful emited CSR</h1>
      <button onClick={() => navigate('/')}>ok</button>
    </>
  )
}