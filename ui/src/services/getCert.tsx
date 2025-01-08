import { CSRType } from "../types/CSR"

const API_URL = 'http://localhost:5000/issue_csr'

interface DataResponse {
  valid: boolean,
  message: string
}

export const getCert = async ({ common_name, organization_name }: CSRType) : Promise<DataResponse> => {
  const bodyRequest = JSON.stringify({
    common_name,
    organization_name
  })

  const request = new Request(API_URL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: bodyRequest
  })

  try {
    const response = await fetch(request)
    const data = await response.json()
    return data
  }

  catch {
    throw new Error('Error in request')
  }
}