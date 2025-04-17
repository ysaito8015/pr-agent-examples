require 'mysql2'

client = Mysql2::Client.new(host: env['DB_HOST'])
results = client.query("SELECT * FROM People WHERE FirstName = 'John'")
puts results.to_a
