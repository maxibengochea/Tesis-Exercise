import { useCSRInfo } from "../hooks/useCSRInfo"

export function Home() {
  const { handleChange, handleSubmit } = useCSRInfo()

  return (
    <>
      <header>
        <h1>ISSUE CSR</h1>
      </header>
      <form onSubmit={handleSubmit}>
        <fieldset>
          <legend>Whats's your organization name</legend>
          <input 
            className="border-8"
            type='text'
            placeholder="Organization name"
            onChange={handleChange}
            name="organization_name"
          />
        </fieldset>
        <fieldset>
          <legend>What's your common name</legend>
          <input 
            type='text'
            placeholder="Organization name"
            onChange={handleChange}
            name="common_name"
          />
        </fieldset>
      </form>
    </>
  )
}