# jekyll-archives writes one page per tag; they are redirect stubs (see _layouts/tag.html), so keep
# them out of the sitemap. Runs after the archives generator and before jekyll-sitemap.
class TagStubsOutOfSitemap < Jekyll::Generator
  priority :low

  def generate(site)
    site.pages.each do |page|
      page.data["sitemap"] = false if page.class.name == "Jekyll::Archives::Archive"
    end
  end
end
