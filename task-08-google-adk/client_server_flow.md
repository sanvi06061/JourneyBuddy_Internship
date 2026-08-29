# Client Server Interaction Lifecycle

1. UI captures the user's refresh event.
2. Client changes state from IDLE to LOADING.
3. Client sends an asynchronous request.
4. Server processes the request.
5. Server returns data or an error.
6. Client updates application state.
7. UI observes the new state.
8. View is re-rendered.

This prevents inconsistent UI behaviour during asynchronous operations.
