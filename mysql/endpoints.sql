SELECT 
endpoints.endpoint,
accessibility.roles 
FROM endpoints join accessibility 
WHERE endpoints.id = accessibility.endpoint_id;
