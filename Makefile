serve:
	python -m http.server --directory .

export:
		for file in notebooks/*; \
		do \
			without_extension=$${file#notebooks/}; \
			without_extension=$${without_extension%.*}; \
			uv run marimo export html-wasm "$$file" -o static/"$$without_extension".html --mode edit; \
		done

