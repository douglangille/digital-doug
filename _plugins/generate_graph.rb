Jekyll::Hooks.register :site, :post_write do |site|
  nodes = []
  edges = Set.new
  seen_pairs = Set.new

  # Build nodes from tags
  site.tags.each do |tag, posts|
    nodes << {
      "id" => tag.downcase.gsub(/\s+/, '-'),
      "label" => tag,
      "size" => posts.length
    }
  end

  # Build edges from co-occurring tags
  site.posts.docs.each do |post|
    tags = post.data['tags'] || []
    tags.each_with_index do |tag, i|
      tags.each_with_index do |other_tag, j|
        if i < j
          pair = [tag.downcase.gsub(/\s+/, '-'), other_tag.downcase.gsub(/\s+/, '-')].sort.join('|')
          unless seen_pairs.include?(pair)
            edges << {
              "source" => tag.downcase.gsub(/\s+/, '-'),
              "target" => other_tag.downcase.gsub(/\s+/, '-')
            }
            seen_pairs << pair
          end
        end
      end
    end
  end

  graph = {
    "nodes" => nodes.sort_by { |n| n["id"] },
    "edges" => edges.to_a
  }

  output_path = File.join(site.dest, 'assets', 'data', 'graph.json')
  FileUtils.mkdir_p(File.dirname(output_path))
  File.write(output_path, JSON.pretty_generate(graph))
  puts "Generated graph: #{output_path}"
end