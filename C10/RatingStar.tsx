import {
    Streamlit,
    StreamlitComponentBase,
    withStreamlitConnection,
    } from "streamlit-component-lib"
    import React, { ReactNode } from "react"
    import { Rating } from '@mui/material';
    interface State {}
    class RatingStar extends StreamlitComponentBase<State> {
    public state = {}

public render = (): ReactNode => {
    return (
    <Rating size="large" defaultValue={3} />
    )
    }
    }
    export default withStreamlitConnection(RatingStar)    