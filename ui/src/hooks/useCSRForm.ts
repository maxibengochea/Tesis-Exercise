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
    const csr = cleanCSR(csrInfo)
    const {valid, message} = await getCert(csr)
  
    if (!valid) 
      return alert(message)
  
    updateSuccessfulIssue(true)
    navigate('successful_issue')
  }

  const cleanCSR = (csr: CSRType): CSRType => {
    const {  common_name, organization_name } = csr

    return {
      common_name: common_name.trim(),
      organization_name: organization_name.trim()
    }
  }

  return {
    handleChange,
    handleSubmit,
    csrInfo
  }
}
