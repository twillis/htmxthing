;;; project setup

;; env var setup example
;; (setenv "SOME_VAR" "some value")

;; venv located one level up from here at .venv
(setq venv-for-project
      (expand-file-name (concat (projectile-project-root) "../.venv")))

(defun project-activate (venv-path)
  (interactive)
  (pyvenv-activate venv-path) ;; one of these works
  (setq pyvenv-activate venv-path))

(project-activate venv-for-project)

(setq projectile-project-test-cmd
      (concat "pipenv run pytest " (projectile-project-root) "tests"))

(setq python-shell-interpreter "ipython"
      python-shell-interpreter-args "-i"
      lsp-pylsp-plugins-pydocstyle-ignore ["D"]

      lsp-pylsp-plugins-flake8-ignore ["E501"])
