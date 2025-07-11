import { test, expect } from "@playwright/test";

test("has title", async ({ page, request }) => {
  await page.goto("https://leetcode.com/problemset");

  await expect(
    page.getByRole("textbox", { name: "Search questions" }),
  ).toBeVisible();

  const todaysDay = new Date().getUTCDate();

  const href = await page
    .getByRole("link", {
      name: `${todaysDay}`,
      exact: true,
    })
    .evaluateAll((els) =>
      els.map((el) => {
        return el.href;
      }),
    );

  await page.goto(href[0]);
  await page.waitForLoadState("networkidle"); // <-  until there are no network connections for at least 500 ms.

  await expect(page.getByText("Description").first()).toBeVisible({
    timeout: 10000,
  });

  await page.getByRole("button", { name: "C++" }).first().click();
  await page.getByText("Python3").first().click();

  await page.waitForTimeout(2000);

  const code = await page
    .locator(".monaco-scrollable-element")
    .locator(".view-line")
    .allInnerTexts();

  const link = page.url();

  code.forEach((c) => console.log("c", c));
  console.log("link", link);

  await page.getByText("Testcase").first().dblclick();

  const cases = await page
    .locator(".flexlayout__tab")
    .getByRole("button", { name: "Case ", exact: false })
    .all();

  const test_cases: string[][] = [];

  for (const ca of cases) {
    await ca.click();
    const values = await page
      .locator("div.flex.h-full.w-full.flex-col.space-y-2")
      .allInnerTexts();

    test_cases.push(values);
  }

  const request_data = { code, test_cases, link };

  await request.post("http://localhost:30123/proxy/apps/leetcode/message", {
    data: request_data,
  });
});

test("get started link", async ({ page }) => {
  await page.goto("https://playwright.dev/");

  // Click the get started link.
  await page.getByRole("link", { name: "Get started" }).click();

  // Expects page to have a heading with the name of Installation.
  await expect(
    page.getByRole("heading", { name: "Installation" }),
  ).toBeVisible();
});
