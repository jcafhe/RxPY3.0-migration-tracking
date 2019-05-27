### operator reworks:
- [ ] `window`:
  - `window(openings: Observable)`
  - `window_when(closing_mapper: Callable[[], Observable])`
  - `window_toggle(openings: Observable, closing_mapper: Callable[[Any], Observable])`
  
- [ ] `buffer`:
  - `buffer(openings: Observable)`
  - `buffer_when(closing_mapper: Callable[[], Observable])`
  - `buffer_toggle(openings: Observable, closing_mapper: Callable[[Any], Observable])`
  
- [ ] `sample`: should be polymorphic i.e. accept an Observable or a time interval `sample(sampler: Union[Observable, RelativeTime)]` or split in:
  - `sample(sampler: Observable)`
  - `sample_time(interval: RelativeTime)`
  
- [ ] `catch`: should be polymorphic i.e. accept an Observable or a callable `catch(handler: Union[Observable, Callable[Exception, Observable], Observable])]` 
