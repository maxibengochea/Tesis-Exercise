import ReactConfetti from "react-confetti"
import { useNavigate } from "react-router-dom"
import { useWindowSize } from "react-use"

export function SuccesfulIssue() {
  const navigate = useNavigate()
  const { width, height } = useWindowSize()

  return (
    <main className="[background:linear-gradient(#1e293b,white)] h-[100vh] flex items-center justify-center">
      <ReactConfetti
        width={width}
        height={height}
      />
      <section className="w-[20%] flex items-center justify-center gap-4 flex-col [box-shadow:_inset_1px_1px_5px_gray,_1px_1px_5px_gray]">
        <h1 className="font-bold text-white text-[25px]">Succesful emited CSR</h1>
        <button 
          className="bg-sky-600 text-white font-bold my-[10px] p-2 hover:bg-sky-900" 
          onClick={() => navigate('/')}
        >
          Ok
        </button>
      </section>
    </main>
  )
}