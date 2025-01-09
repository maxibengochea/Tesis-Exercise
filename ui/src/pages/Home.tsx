import { useId } from "react"
import { useCSRForm } from "../hooks/useCSRForm"

interface FieldFormProps {
  children: string,
  id: string, 
  name: string,
  onChange(e: React.ChangeEvent<HTMLInputElement>): void,
  placeholder?: string
}

export function Home() {
  const { handleChange, handleSubmit } = useCSRForm()
  const commonNameId = useId()
  const organizationNameId = useId()

  return (
    <main className="[background:linear-gradient(#1e293b,white)] h-[100vh] flex items-center justify-center">
      <form 
        className="h-[80%] w-[80%] flex items-center justify-center rounded-[12px] [box-shadow:_inset_1px_1px_3px_black,_1px_1px_3px_black]"
        onSubmit={handleSubmit}>
        <fieldset className="border-solid border-[1px] border-gray-500 h-[90%] w-[90%] flex flex-col justify-between items-center">
          <legend className="mx-[auto] px-2 font-bold text-white text-[25px]">ISSUE CSR</legend>
          <div className="h-[75%] w-full flex flex-col justify-evenly items-center">
            <FieldForm
              id={organizationNameId}
              name="organization_name"
              onChange={handleChange}
            >
              organization name:
            </FieldForm>
            <FieldForm
              id={commonNameId}
              name="common_name"
              onChange={handleChange}
              placeholder="example: node1..."
            >
              common name:
            </FieldForm>
          </div>
          <button className="bg-sky-600 text-white font-bold mb-[10px] p-2 hover:bg-sky-900" >Issue CSR</button>
        </fieldset>
      </form>
    </main>
  )
}

const FieldForm = ({ id, name, onChange, children, placeholder }: FieldFormProps) => {
  return (
    <div className="w-full flex flex-col justify-center items-start gap-2">
      <label
        className="px-5 text-white font-bold"
        htmlFor={id}
      >
        {children}
      </label>
      <input
        className="px-5 py-1 mx-5 w-[95%] text-black"
        id={id} 
        type='text'
        onChange={onChange}
        name={name}
        placeholder={placeholder ?? ''}
      />
    </div>
  )
}