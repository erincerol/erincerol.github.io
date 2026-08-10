# Privacy Policy Page Reference Implementation

Each app loads `Resources/Raw/privacy.json` at startup and renders it in a `CollectionView`. No hardcoded XAML needed.

## PrivacyPolicyPage.xaml

```xml
<?xml version="1.0" encoding="utf-8" ?>
<ContentPage xmlns="http://schemas.microsoft.com/dotnet/2021/maui"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             x:Class="TheApp.Pages.PrivacyPolicyPage"
             Title="Privacy Policy"
             BackgroundColor="{AppThemeBinding Light={StaticResource Cream}, Dark={StaticResource DarkBg}}">

  <Grid RowDefinitions="*,Auto" Padding="20,0">
    <CollectionView ItemsSource="{Binding Sections}" SelectionMode="None">
      <CollectionView.ItemTemplate>
        <DataTemplate>
          <VerticalStackLayout Padding="0,28,0,0" Spacing="8">
            <Label Text="{Binding Heading}" 
                   FontFamily="Georgia"
                   FontSize="18"
                   FontAttributes="Bold"
                   TextColor="{AppThemeBinding Light={StaticResource DeepText}, Dark={StaticResource LightText}}" />
            <Label Text="{Binding Body}" 
                   FontSize="14"
                   LineHeight="1.6"
                   TextColor="{AppThemeBinding Light={StaticResource MutedText}, Dark={StaticResource MutedTextDark}}" />
          </VerticalStackLayout>
        </DataTemplate>
      </CollectionView.ItemTemplate>
    </CollectionView>

    <!-- Online version link -->
    <VerticalStackLayout Grid.Row="1" Padding="0,20,0,20" Spacing="12">
      <BoxView HeightRequest="1" Color="{AppThemeBinding Light=#E0E0E0, Dark=#333}" />
      <Label Text="View the latest version online" 
             FontSize="13"
             TextDecorations="Underline"
             TextColor="{StaticResource Accent}">
        <Label.GestureRecognizers>
          <TapGestureRecognizer Command="{Binding OpenOnlineCommand}" />
        </Label.GestureRecognizers>
      </Label>
      <Label Text="{Binding UpdatedText}" 
             FontSize="12"
             TextColor="{AppThemeBinding Light={StaticResource Muted}, Dark={StaticResource MutedDark}}" />
    </VerticalStackLayout>
  </Grid>
</ContentPage>
```

## PrivacyPolicyViewModel.cs

```csharp
using System.Collections.ObjectModel;
using System.Text.Json;
using System.Text.Json.Serialization;
using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;

namespace TheApp.ViewModels;

public partial class PrivacyPolicyViewModel : ObservableObject
{
    private readonly IStringLocalizer<PrivacyPolicyViewModel> _localizer;

    [ObservableProperty]
    ObservableCollection<PrivacySection> sections = [];

    [ObservableProperty]
    string updatedText = "";

    private const string PrivacyJsonResource = "privacy.json";
    private const string AppStorePrivacyUrl = "https://eritech.studio/privacy-policies/{slug}.html";

    public PrivacyPolicyViewModel(IStringLocalizer<PrivacyPolicyViewModel> localizer)
    {
        _localizer = localizer;
    }

    public async void OnAppearing()
    {
        await LoadPrivacyPolicy();
    }

    private async Task LoadPrivacyPolicy()
    {
        try
        {
            // Load privacy.json from Resources/Raw
            using var stream = await FileSystem.OpenAppPackageFileAsync(PrivacyJsonResource);
            using var reader = new StreamReader(stream);
            var json = await reader.ReadToEndAsync();

            var policy = JsonSerializer.Deserialize<PrivacyPolicy>(json);
            if (policy == null) return;

            Sections = new ObservableCollection<PrivacySection>(policy.Sections);

            // Format the "Last Updated" date
            if (DateTime.TryParse(policy.Updated, out var date))
            {
                UpdatedText = $"Last Updated: {date:MMMM d, yyyy}";
            }
        }
        catch (Exception ex)
        {
            // Log or handle error; privacy policy is critical but not fatal to app operation
            System.Diagnostics.Debug.WriteLine($"Failed to load privacy policy: {ex.Message}");
        }
    }

    [RelayCommand]
    async Task OpenOnline()
    {
        try
        {
            // Replace {slug} with your app's identifier (e.g., "the-bake-log")
            var url = AppStorePrivacyUrl.Replace("{slug}", "your-app-slug");
            await Launcher.Default.OpenAsync(url);
        }
        catch (Exception ex)
        {
            // Fallback silent fail or log to analytics
            System.Diagnostics.Debug.WriteLine($"Failed to open privacy URL: {ex.Message}");
        }
    }
}

public class PrivacyPolicy
{
    [JsonPropertyName("sections")]
    public List<PrivacySection> Sections { get; set; } = [];

    [JsonPropertyName("updated")]
    public string Updated { get; set; } = "";
}

public class PrivacySection
{
    [JsonPropertyName("heading")]
    public string Heading { get; set; } = "";

    [JsonPropertyName("body")]
    public string Body { get; set; } = "";
}
```

## PrivacyPolicyPage.xaml.cs

```csharp
namespace TheApp.Pages;

public partial class PrivacyPolicyPage : ContentPage
{
    public PrivacyPolicyPage(PrivacyPolicyViewModel viewModel)
    {
        InitializeComponent();
        BindingContext = viewModel;
    }

    protected override void OnAppearing()
    {
        base.OnAppearing();
        if (BindingContext is PrivacyPolicyViewModel vm)
            vm.OnAppearing();
    }
}
```

## Registration (MauiProgram.cs)

```csharp
builder
    .Services
    .AddSingleton<PrivacyPolicyPage>()
    .AddSingleton<PrivacyPolicyViewModel>();
```

## Notes

- The `privacy.json` is automatically copied by `scripts/build-privacy-policies.js` on every build.
- Edit the source markdown in `/Users/erinc/Documents/repos/erincerol.github.io/privacy/{app-slug}.md` — the script regenerates both the web HTML and the app JSON.
- The "View the latest version online" link points to the stable URL on the website.
- Markdown formatting (bold, italics) in the JSON body persists as plain text in the app — if you need rich text, convert the `body` field to HTML or use a markdown renderer.
