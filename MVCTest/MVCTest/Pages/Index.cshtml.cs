using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.EntityFrameworkCore;
using MVCTest.Models;
using RazorPagesMovie.Models;

namespace MVCTest.Pages.Movies
{
    public class IndexModel : PageModel
    {
        private readonly MVCTest.Models.MVCTestContext _context;

        public IndexModel(MVCTest.Models.MVCTestContext context)
        {
            _context = context;
        }

        public IList<Movie> Movie { get;set; }

        public async Task OnGetAsync()
        {
            Movie = await _context.Movie.ToListAsync();
        }
    }
}
