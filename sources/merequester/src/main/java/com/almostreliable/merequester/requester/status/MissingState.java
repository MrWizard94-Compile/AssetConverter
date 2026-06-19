package com.almostreliable.merequester.requester.status;

public class MissingState extends BlockingState {

    MissingState() {}

    @Override
    public RequestStatus type() {
        return RequestStatus.MISSING;
    }
}
