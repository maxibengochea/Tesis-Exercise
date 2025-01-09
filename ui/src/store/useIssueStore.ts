import { create } from "zustand"

interface State {
  successfulIssue: boolean,
  updateSuccessfulIssue(action: boolean): void
}

export const useIssueStore = create<State>(set => ({
  successfulIssue: false,
  updateSuccessfulIssue: (action: boolean) => set(({successfulIssue: action}))
}))