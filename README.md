### Split operators:
- [ ] `buffer`:
  - `buffer(openings: Observable)`
  - `buffer_when(closing_mapper: Callable[[], Observable])`
  - `buffer_toggle(openings: Observable, closing_mapper: Callable[[Any], Observable])`
  
- [ ] `sample`:
  - `sample(sampler: Observable)`
  - `sample_time(interval: RelativeTime)`
  
