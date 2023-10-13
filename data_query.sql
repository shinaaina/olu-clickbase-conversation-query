SELECT 
    agent_id,
    AVG(call_duration_sec) AS avg_call_length,
    quantile(0.9)(call_duration_sec) AS percentile_90_call_length
FROM conversations
WHERE toDate(call_start) = today()
GROUP BY agent_id;