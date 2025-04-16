require 'mysql2'

client = Mysql2::Client.new(host: env['DB_HOST'])
results = client.query("SELECT * FROM Persons WHERE FirstName = 'John'" ORDER BY CreatedAt DESC)
puts results.to_a
