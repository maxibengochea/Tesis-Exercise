import { useState } from "react"
import { CSRType } from "../types/CSR"
import { getCert } from "../services/getCert"
import { useNavigate } from "react-router-dom"
import { useIssueStore } from "../store/useIssueStore"

export function useCSRForm() {
  const navigate = useNavigate()
  const updateSuccessfulIssue = useIssueStore(state => state.updateSuccessfulIssue)

  const [csrInfo, setcsrInfo] = useState<CSRType>({
    common_name: '',
    organization_name: ''
  })
  
  const handleChange = (e:  React.ChangeEvent<HTMLInputElement>) => {
    setcsrInfo(prevState => ({
      ...prevState,
      [e.target.name]: e.target.value
    }))
  }
  
  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault()
    const {valid, message} = await getCert(csrInfo)
  
    if (!valid) 
      return alert(message)
  
    updateSuccessfulIssue(true)
    navigate('successful_issue')
  }

  return {
    handleChange,
    handleSubmit,
    csrInfo
  }
}
