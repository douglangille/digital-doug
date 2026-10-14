# Posts without an `excerpt:` get a `description` made from their first sentence, so cards and
# link previews have something to show. It is never used as a subtitle (the layouts only show a
# front-matter excerpt there). To write a real one, add `excerpt:` to the post.
Jekyll::Hooks.register :documents, :pre_render do |doc|
  next unless doc.collection.label == "posts"
  next if doc.data["excerpt"].is_a?(String) || doc.data["description"]

  text = doc.content.sub(/\A\s*#\s+.*\n/, "")
  para = text.split(/\n{2,}/).map(&:strip).find { |p| !p.empty? && p !~ /\A(\{%|<|!\[|---|\*\*\*|>|#|\[SCREENSHOT)/ }
  next unless para

  para = para.gsub(/!\[[^\]]*\]\([^)]*\)/, "").gsub(/\[([^\]]+)\]\([^)]*\)/, '\1').gsub(/[*_`]/, "").gsub(/\s+/, " ").strip
  sentence = para[/\A.{40,}?[.!?](?=\s|\z)/m] || para
  if sentence.length > 160
    sentence = sentence[0, 160].sub(/\s+\S*\z/, "") + "…"
  end
  doc.data["description"] = sentence
end
