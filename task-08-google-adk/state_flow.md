# Google ADK - State Driven Client Server Flow

## Scenario

A user initiates a data refresh from an application view.

## State Machine

IDLE
 ↓
REFRESH_REQUESTED
 ↓
LOADING
 ↓
NETWORK_REQUEST
 ↓
SUCCESS / ERROR

SUCCESS
 ↓
UPDATE_DATA
 ↓
RENDER_VIEW

ERROR
 ↓
DISPLAY_ERROR
 ↓
RETURN_TO_IDLE

## Important Principle

The UI should not assume that the asynchronous request succeeded.

The state changes only after the network operation produces a result.

## Example

User taps Refresh
       ↓
UI event captured
       ↓
Async request started
       ↓
Loading indicator displayed
       ↓
Server response received
       ↓
Application state updated
       ↓
UI re-rendered
