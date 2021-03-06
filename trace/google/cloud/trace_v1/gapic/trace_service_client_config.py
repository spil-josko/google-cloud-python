config = {
    "interfaces": {
        "google.devtools.cloudtrace.v1.TraceService": {
            "retry_codes": {
                "idempotent": ["DEADLINE_EXCEEDED", "UNAVAILABLE"],
                "non_idempotent": []
            },
            "retry_params": {
                "default": {
                    "initial_retry_delay_millis": 100,
                    "retry_delay_multiplier": 1.2,
                    "max_retry_delay_millis": 1000,
                    "initial_rpc_timeout_millis": 20000,
                    "rpc_timeout_multiplier": 1.5,
                    "max_rpc_timeout_millis": 30000,
                    "total_timeout_millis": 45000
                }
            },
            "methods": {
                "PatchTraces": {
                    "timeout_millis": 60000,
                    "retry_codes_name": "idempotent",
                    "retry_params_name": "default"
                },
                "GetTrace": {
                    "timeout_millis": 60000,
                    "retry_codes_name": "idempotent",
                    "retry_params_name": "default"
                },
                "ListTraces": {
                    "timeout_millis": 60000,
                    "retry_codes_name": "idempotent",
                    "retry_params_name": "default"
                }
            }
        }
    }
}
