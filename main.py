from neo4j import GraphDatabase

uri = "neo4j+s://e8ee760b.databases.neo4j.io:7687"
user = "neo4j"
password = "EpXxYsQ5VHFo_z-ovFgZoHmQKUP4FG1EOl8igt45haQ"

driver = GraphDatabase.driver(uri, auth=(user, password))

# Function to run a Cypher query
def run_query(query):
    with driver.session() as session:
        result = session.run(query)
        # Convert the result to a list before returning it
        return list(result)

# Example query
query1 = "MATCH (n) RETURN count(n) AS nodeCount"
query2 = "MATCH (n:Label) RETURN count(n) AS labeledNodeCount"

# Run the queries
result1 = run_query(query1)
result2 = run_query(query2)

# Process the results
print("Result 1:")
for record in result1:
    print(record["nodeCount"])

print("\nResult 2:")
for record in result2:
    print(record["labeledNodeCount"])

# Close the driver when done
driver.close()
